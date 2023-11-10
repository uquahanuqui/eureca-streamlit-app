import streamlit as st

#타이틀 & 이모티콘
st.title("Home :snowman:")

#구분선
st.divider()

#일반 글씨
st.header("Lens in Gray")
st.write("Team 6 : uquahanuqui :christmas_tree:")
    
#이미지 삽입
from PIL import Image

# Use a raw string for the file path
image_path = r"/jwy.jpg"

# Load the image into the Streamlit app
image = Image.open("https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg")

# Display the image in the Streamlit app
st.image(image, caption='A caption for your image', use_column_width='always')

#눈내림
st.snow()

#검색창
st.markdown("---")
search_query = st.text_input("Search :mag:")
