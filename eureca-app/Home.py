import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>☃️Lens in Gray☃️</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#일반 글씨
st.write("Team 6 : uquahanuqui :christmas_tree:")

#이미지 첨부
img_url = "https://newsimg.sedaily.com/2023/08/24/29TJ6B9OLG_2.jpg"
st.image(img_url)


#눈내림
st.snow()

#검색창
st.markdown("---")
search_query = st.text_input("Search :mag:")
