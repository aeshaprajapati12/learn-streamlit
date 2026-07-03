import streamlit as st
st.title("Hello Aesha!!")
st.header("This is a header line!!")
st.subheader("This is a subheader line!!")

st.text("Welcome to Akash Technology!")

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")

st.write(range(10))

if st.checkbox("Show/Hide"):
    st.info("Showing the widget")


status = st.radio("Select Gender: ",("Male","Female"))
if status == 'Male':
    st.success("Male")

else:
    st.success("Female")

hobby = st.selectbox("Hobbies: ",['Reading','Learning','Sport'])
a = st.write("My Hobby Is : ",hobby)
st.success(hobby)

hobbies = st.multiselect("Hobbies: ",['Reading','Learning','Sport'])
a = st.write("My Hobbies Is : ",len(hobbies))
b = st.write("My Hobbies Is : ",hobbies)
st.success(hobbies)

st.button("Click Me")
if st.button("About"):
    st.info("Welcome to Akash Technology")

name = st.text_input("Enter Your Name :","Type Here...")
if st.button("Submit"):
    result = name.title()
    st.success(result)

fname = st.text_input("Enter Your Name :")
if st.button("ClickMe"):
    st.title(fname)


no1 = st.text_input("Enter no :")
if(st.button("Click")):
    if(int(no1) % 2 == 0):
        st.text("No is Even.")
    else:
        st.text("No is Odd.")

level = st.slider("Select the level",1,5)
st.text('Selected : {}'.format(level))


st.number_input("pick a number",0,10)
st.text_input("Email address")
st.date_input("DOB")
st.time_input("School time")
st.text_area("description")
st.file_uploader("Upload photo")
st.color_picker("Choose your favorite color")

import time
st.balloons()
st.subheader("progress-bar")
st.progress(10)

st.subheader("Wait for the execution")
with st.spinner("Wait for it...."):
    time.sleep(2)

st.title("sum of 2 numbers")
n1 = st.number_input("Enter n1")
n2 = st.number_input("Enter n2")
ans = n1 + n2

if st.button("Calculate sum"):
    st.text("sum is  {}.".format(ans))


st.title('Mini-Calculator')
n1 = st.number_input("Enter num1")
n2 = st.number_input("Enter num2")
col1, col2, col3, col4 = st.columns(4)
with col1:
    Sum = st.button('Sum +')
with col2:
    Sub = st.button('Sub -')
with col3:
    Mul = st.button('Mul *')
with col4:
    Div = st.button('Div /')
if Sum:
    ans = int(n1) + (n2)
    st.text("Sum is  {}.".format(ans))
if Sub:
    ans = n1 - n2
    st.text("Subtraction is  {}.".format(ans))
if Mul:
    ans = n1 * n2
    st.text("Multiplication is  {}.".format(ans))
if Div:
    ans = n1 / n2
    st.text("Division is  {}.".format(ans))


st.title('Mini_Calculator')
# TAKE INPUT 
n1 = st.number_input("Enter 1")
n2 = st.number_input("Enter 2")
action = st.radio('Select your action: ',
('Sum', 'Sub', 'Mul', 'Div'), horizontal=True)
if (action == 'Sum'):
    ans = n1 + n2
    st.success("Sum is {}.".format(ans))
if (action == 'Sub'):
    ans = n1 - n2
    st.success("Subtraction is {}.".format(ans))
if (action == 'Mul'):
    ans = n1 * n2
    st.success("Multiplication is {}.".format(ans))
if (action == 'Div'):
    ans = n1 / n2
    st.success("Division is {}.".format(ans))
