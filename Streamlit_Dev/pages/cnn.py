import streamlit as st 
import tensorflow as tf 
st.set_option('description.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('/content/cnn_3_model.hdf5')
  return model
model = load_model()
st.write("""
        # Food 101 Classification 
        """)
file = st.file_uploader("Please upload an flower image", type=["jpg","png"])
import cv2 
from PIL import Image, ImageOps
import numpy as np 
def import_and_predict(image_dataset_from_directory, model_2):
  size = (223,223)
  image = ImageOps.fit(image_dataset_from_directory, Image.ANTIALIAS)
  img = np.asarray(image)
  img_reshape = img[np.newaxis,...]
  prediction = model_2.predict(img_reshape)
  return prediction

if file is None:
  st.text("Please upload an image file")
else:
  image = Image.open(file)
  st.image(image, use_column_width=True)
  predictions = import_and_predict(image,model)
  class_names=["chicken_curry","chicken_wings","fried_rice","grilled_salmon",
  "hamburger","ice_cream","pizza","ramen","steak","sushi"]
  string = "This image most likely is: "+class_names[np.argmax(predictions)]
  st.success(string)
