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
# cnn_model = tf.keras.models.load_model("cnn_3_model.hdf5")
st.set_page_config(
	page_title = "CNN - Project #7 - Image Predictor",
	page_icon="👨‍⚕️")

# st.set_option('description.showfileUploaderEncoding', False)
@st.cache() #allow_output_mutation=True

def load_model():
	model = tf.keras.models.load_model("cnn_3_model.hdf5")
	return model
model = load_model()
st.write("""
		# CNN Sample Project for 101 Food UDEMY Class
		""")
file = st.file_uploader("Please upload an flower image", type=["jpg","png"])

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
