import streamlit as st
from PIL import Image


st.title("BMI Calculator")
img = Image.open("bmi.jpg")
st.image(img)

# link credit
url = "https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html"
st.markdown("Image Credit : [CDC](%s)" % url) # st.write()  we also use


# input some feature
weight = st.number_input("Weight in KG")
height = st.number_input("Height in Meter")


x = weight
y= height

# # bmi calculation 
try:
	bmi = x / y ** 2
	st.success(f"Your BMI : {bmi}")
except ZeroDivisionError as e:
	results = 0
finally:
	st.subheader("Happy Learning")	

# Follow me link

github_url = "https://github.com/shivji-sj"
linkedin_url ="https://www.linkedin.com/in/shivji-881449205/recent-activity/"
medium_url = "https://medium.com/@sjshivji"

st.header("Follow Me : ")

col1, col2, col3 = st.columns(3)

with col1:
	st.markdown("[GitHub](%s)" % github_url)
with col2:
	st.markdown("[LinkedIn](%s)" % linkedin_url)
with col3:
	st.markdown("[Medium](%s)" % medium_url)
