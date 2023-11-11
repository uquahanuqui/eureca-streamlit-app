import streamlit as st

# 타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>☃️Lens in Gray☃️</h1>", unsafe_allow_html=True)

# 구분선
st.markdown("---")

# 일반 글씨
st.write("Team 6 : uquahanuqui 🎄")

# 이미지 추가
image_url = "jwy.jpeg"  # 이미지 파일의 경로를 정확하게 지정해주세요.
st.image(image_url, caption="Image Description")

# 검색창
search_query = st.text_input("Search :mag:")
