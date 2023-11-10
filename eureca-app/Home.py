import streamlit as st

#사이드바
st.sidebar.markdown("Home :snowman:")

#타이틀 & 이모티콘
st.title("Home :snowman:")

#구분선
st.divider()

#일반 글씨
st.header("AI personal lens recommendation platform")
st.write("Team 6 : uquahanuqui :christmas_tree:")
    
#이미지 삽입

#눈내림
st.snow()

#검색창
st.markdown("---")
search_query = st.text_input("Search :mag:")
