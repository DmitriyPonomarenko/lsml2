import streamlit as st
from PIL import Image
import requests
import base64

st.set_page_config(layout="centered", page_title="FOOD101")


def set_bg_hack(main_bg):
    main_bg_ext = "jpeg"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


set_bg_hack("background.jpg")
st.title(f":red[Image Classification Task]")

upload = st.file_uploader(
    label=f"Load the image of your object",
    type=['png', 'jpeg', 'jpg'])

c1, c2 = st.columns(2)

if upload:
    files = {"file": upload.getvalue()}
    req = requests.post("http://webserver:5000/predict", files=files)
    result = req.json()
    rec = result["predictions"]
    c1.image(Image.open(upload))
    c2.write(f"## :green[This is... {rec}!]")
    c2.write(f"**Execution time: {result['time']} seconds**")
