import streamlit as st

#타이틀 & 이모티콘
st.title("안뇽! :snowman:")

#구분선
st.divider()

#일반 글씨
st.header("AI 퍼스널 렌즈 추천 플랫폼")
st.write("6조 : 유쾌한육회")

st.divider()

#버튼 클릭
clicked=st.button("Go Shopping")

#이미지 삽입

#사이드바
with st.sidebar:
        "Home"
        "Shop"
        "AI Personal"
        "Community" 
        "Notice"
