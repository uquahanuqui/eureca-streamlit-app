import streamlit as st

#타이틀 & 이모티콘
st.title("Home :snowman:")

#구분선
st.divider()

#일반 글씨
st.header("Lens in Gray")
st.write("Team 6 : uquahanuqui :christmas_tree:")
    
#이미지 삽입
import streamlit as st
from PIL import Image

image_path = "C:\Users\User\Downloads\jwy.jpg"
image = Image.open(image_path)

#눈내림
st.snow()

#검색창
st.markdown("---")
search_query = st.text_input("Search :mag:")
