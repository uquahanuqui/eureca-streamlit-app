import streamlit as st

#타이틀 & 이모티콘
st.title("안뇽! :fish_cake: :yellow_heart: :snowman:")

#일반 글씨
st.header("유쾌한육회")
st.write("우리는 6조")
st.text("렌즈추천사이트")

#버튼 클릭
clicked=st.button("click")

#이미지 삽입

#사이드바
with st.sidebar:
    shop=st.text_input(
        "Shop"
    )
    ai=st.text_input(
        "AI Personal"
    )
    community=st.text_input(
        "Community"
    )
    notice=st.text_input(
        "Notice"
    )
