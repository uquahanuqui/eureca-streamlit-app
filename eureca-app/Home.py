import streamlit as st

#타이틀 & 이모티콘
st.title("Home :snowman:")

#구분선
st.divider()

#일반 글씨
st.header("AI 퍼스널 렌즈 추천 플랫폼")
st.write("6조 : 유쾌한육회")

st.divider()

#버튼 클릭
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("Lens-me", "https://www.lens-me.com/shop/")

with col2:
    st.link_button("O-lens", "https://o-lens.com/")

with col3:
    st.link_button("Idol-lens", "https://www.i-dol.kr/")

with col4:
    st.link_button("HapaKristin", "https://hapakristin.co.kr/")
    
#이미지 삽입

#눈내림
st.snow()

#페이지
def main_page():
    st.markdown("Home")
    st.sidebar.markdown("Home")

def page2():
    st.markdown("Shop")
    st.sidebar.markdown("Shop")

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}
