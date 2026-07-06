import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Nature Images",
    page_icon='🌿',
    layout="wide"
)

st.title("🌿 Nature Images")
st.write("Here are multiple nature pictures!")
st.divider()

img1 = Image.open("1.jpg").resize((300,200))
img2 = Image.open("2.jpg").resize((300,200))
img3 = Image.open("3.jpg").resize((300,200))

col1, col2, col3 = st.columns(3)

with col1:
    st.image(img1, use_container_width=True)
    st.subheader("🌿Nature-1")
    st.write("Greenery!")
    c = st.selectbox("Choice",["Greenery","Horrifying view!","Beautiful sunrise"])
    a = st.success(c)

with col2:
    st.image(img2, use_container_width=True)
    st.subheader("🌿Nature-2")
    st.write("Horrifying view!")
    c = st.selectbox("Choice1",["Greenery","Horrifying view!","Beautiful sunrise"])
    a = st.success(c)

with col3:
    st.image(img3, use_container_width=True)
    st.subheader("🌿Nature-3")
    st.write("Beautiful sunrise!")
    c = st.selectbox("Choice2",["Greenery","Horrifying view!","Beautiful sunrise"])
    a = st.success(c)
    

st.divider()

col4, col5, col6 = st.columns(3)

st.divider()

with col4:
    st.image(img1, use_container_width=True)
    st.subheader("🌿Nature-4")
    st.write("Greenery!")
    x = st.selectbox("Choice3",["Greenery","Horrifying view!","Beautiful sunrise"])
    y = st.success(x)

with col5:
    st.image(img2, use_container_width=True)
    st.subheader("🌿Nature-5")
    st.write("Horrifying view!")
    z = st.selectbox("Choice4",["Greenery","Horrifying view!","Beautiful sunrise"])
    s = st.success(z)

with col6:
    st.image(img3, use_container_width=True)
    st.subheader("🌿Nature-6")
    st.write("Beautiful sunrise!")
    v = st.selectbox("Choice5",["Greenery","Horrifying view!","Beautiful sunrise"])
    k = st.success(v)



