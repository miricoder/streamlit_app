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

# cnn_model = pickle.load(open("/Users/miralimirzayev/Desktop/McCombs_Bootcamp/cohortDec17/projects/Streamlit_Dev/CNN_Model/saved_model.pb","rb"))
# cnn_model = tf.keras.models.load_model("/Users/miralimirzayev/Desktop/McCombs_Bootcamp/cohortDec17/projects/Streamlit_Dev/CNN_Model/saved_model.pb")
# cnn_model = tf.keras.models.load_model("/Users/miralimirzayev/Desktop/McCombs_Bootcamp/cohortDec17/projects/Streamlit_dev/pages/cnn_3_model.hdf5")
# cnn_model = tf.keras.models.load_model("/Users/miralimirzayev/Desktop/McCombs_Bootcamp/cohortDec17/streamlit_app/models/cnn_3_model.hdf5")
cnn_model = tf.keras.models.load_model("cnn_3_model.hdf5")
st.set_page_config(
	page_title = "CNN - Project #7 - Image Predictor",
	page_icon="👨‍⚕️")