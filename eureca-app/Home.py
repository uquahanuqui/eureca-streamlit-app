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
st.link_button("Lens-me", "https://www.lens-me.com/shop/")
st.link_button("O-lens", "https://o-lens.com/")
st.link_button("Idol-lens", "https://www.i-dol.kr/")
st.link_button("HapaKristin", "https://hapakristin.co.kr/")

#이미지 삽입

#눈내림
st.snow()

#페이지
def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}
