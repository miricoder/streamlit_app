# %writefile cnn.py 
import time 
import requests 
import pickle 
import streamlit as st 
from PIL import Image
from streamlit_lottie import st_lottie 
from streamlit_lottie import st_lottie_spinner
import base64 
from streamlit.components.v1 import html 
import tensorflow as tf 
from tensorflow.keras.applications.imagenet_utils import decode_predictions
# import cv2 
from PIL import Image, ImageOps 
import numpy as np
from inference import infer
#### Inference function that outputs  dish names, the places of origin and ingredients





st.set_page_config(page_icon="", page_title="<<<<<<CNN SAMPLE>>>>>>")




def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://raw.githubusercontent.com/adhok/SeeFood/main/luxury-ornamental-mandala-design-background_1159-6794.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 





st.markdown("<h1 style='text-align: center; color: orange;'>Khana Dekho (🇮🇳 SeeFood)</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: orange;'>A EfficientNetV2 neural network trained to recognize 85 types of Indian Food using the data found <a href = 'https://www.kaggle.com/datasets/iamsouravbanerjee/indian-food-images-dataset'> here. </a> </h4>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; color: orange;'>We present the top five predictions and display their ingredients and region of origin.</h4>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1,18,1])


img = 0

def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image




# Uploading the File to the Page
uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png','jpeg'])

# with col1:
#         st.write(' ')


with col2:



    if uploadFile is not None:


        img = load_image(uploadFile)


        with st.spinner('Wait for it...'):

            list_of_predictions,list_of_prep_times,list_of_regions,list_of_ingredients,pred_prob = infer(uploadFile)
            st.image(img)
            time.sleep(1)





        list_of_predictions = [i.replace('_',' ') for i in list_of_predictions]

        
        st.markdown("<p style='text-align: center; color: white;'>The most likely foods are as follows 👇.</p>", unsafe_allow_html=True)

        if pred_prob[0] > 0.0:
            
            
            st.markdown("""
  #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>  
""".format(list_of_predictions[0],list_of_prep_times[0],list_of_regions[0],list_of_ingredients[0]),  unsafe_allow_html=True)
            


        if pred_prob[1] > 0 :
            st.markdown("""
  #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>  
""".format(list_of_predictions[1],list_of_prep_times[1],list_of_regions[1],list_of_ingredients[1]),  unsafe_allow_html=True)


        if pred_prob[2] > 0:
        
            st.markdown("""
  #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>
""".format(list_of_predictions[2],list_of_prep_times[2],list_of_regions[2],list_of_ingredients[2]),  unsafe_allow_html=True)


        if pred_prob[3] > 0:
        
            st.markdown("""
  #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>
""".format(list_of_predictions[3],list_of_prep_times[3],list_of_regions[3],list_of_ingredients[3]),  unsafe_allow_html=True)


        if pred_prob[4] > 0:
        
            st.markdown("""
  #### <p style="color:white">* This is {} . It takes {} minutes to prepare. The cuisine is based in {} India. The ingredients are {} .</p>  
""".format(list_of_predictions[4],list_of_prep_times[4],list_of_regions[4],list_of_ingredients[4]),  unsafe_allow_html=True)
        
        








        #st.write("Image Uploaded Successfully")
        st.markdown("<p style='text-align: center; color: white;'>Image Uploaded Successfully</p>", unsafe_allow_html=True)
    else:
        #st.write("Make sure you image is in JPG/PNG Format.")
        
        st.markdown("<p style='text-align: center; color: white;'>Make sure you image is in JPG/PNG Format.</p>", unsafe_allow_html=True)

