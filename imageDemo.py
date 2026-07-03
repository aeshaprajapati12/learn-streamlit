import streamlit as st
from PIL import Image

img = Image.open("1.jpg")
st.image(img,width=200)

import streamlit as st
from PIL import Image

img1 = Image.open("1.jpg")
img2 = Image.open("2.jpg")
img3 = Image.open("3.jpg")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(img1, width=200)

with col2:
    st.image(img2, width=200)

with col3:
    st.image(img3, width=200)

import streamlit as st
from PIL import Image

img1 = Image.open("1.jpg")
img2 = Image.open("2.jpg")
img3 = Image.open("3.jpg")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(img1, use_container_width=True)

with col2:
    st.image(img2, use_container_width=True)

with col3:
    st.image(img3, use_container_width=True)