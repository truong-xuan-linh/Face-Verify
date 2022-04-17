from email import message
import streamlit as st
import requests
import cv2
import numpy as np
import math
import keras
import matplotlib.pyplot as plt
from PIL import Image
import os
import cv2
import streamlit as st
from check_valid import check_valid
from check_user import check_user
from keras.models import load_model
import gdown

if "model.h5" not in os.listdir("./"):
    url = "https://drive.google.com/uc?id=1-GztQP5wlqfjz1llOBZrLqV-DcWip24S"
    output = "./model.h5"
    gdown.download(url, output, quiet=False)
model = load_model("./model.h5")
#os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
# icon_img = Image.open("./icon.png")
# st.set_page_config(layout="centered", page_title="Diabetic Retinopathy Detection", page_icon=icon_img )
st.markdown("<h1 style='text-align: center; color: red;'>FACE VERIFY</h1>", unsafe_allow_html=True)

hide_menu_style = """
<style>
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html= True)

list_user = os.listdir("./users")

user_name = st.text_input('Enter your user name', '')
cap = False
mess = ""
st.write(f'We use your face as the password')

FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

# Login = st.button('Log in')
# Signup = st.button('Sign up')



while not cap:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    user_pass = frame
    try:
        if st.button('Log in'):
            if user_name not in list_user:
                st.write("Wrong user name. Please enter again")
                continue
            img_crop, check = check_valid(user_pass, model)
            if not check:
                st.write(img_crop)
                continue
            else:
                print("AAAAAAAAAAA")
                if check_user(img_crop, user_name):
                    st.write(f"Successfull log in. Welcom {user_name}")
                else:
                    st.write("Wrong face")

    except:
        pass

    try:
        if st.button('Sign up'):
            if user_name in list_user:
                st.write("User already exist")
                continue
            img_crop, check = check_valid(user_pass, model)
            
            if not check:
                st.write(img_crop)
                continue
            os.makedirs("./users/"+user_name)
            cv2.imwrite("./users/"+user_name+"/"+user_name+".jpg",img_crop[:,:,::-1])
            st.write("Create account successful")
    except:
        pass




###################