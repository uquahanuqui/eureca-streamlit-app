import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>☃️Lens in Gray☃️</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#일반 글씨
st.write("Team 6 : uquahanuqui :christmas_tree:")

#이미지 첨부
img_url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.blog.naver.com%2Feorudspt%2F222875305727&psig=AOvVaw2fgtJ1No-WUXQTWXt284fR&ust=1699936205915000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCJCWx4CSwIIDFQAAAAAdAAAAABAD"
st.image(image_url)

#눈내림
st.snow()

#검색창
st.markdown("---")
search_query = st.text_input("Search :mag:")
