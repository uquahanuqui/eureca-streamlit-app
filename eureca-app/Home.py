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

#페이지
pip install st_pages
from st_pages import Page, Section, show_pages, add_page_title

add_page_title("LENS IN GRAY")

show_pages(
    [
        Page("Home.py", "Home"),
        Section(name="Shop"),
        page("Lens-me"),
        page("O-lens"),
        page("Idol-lens"),
        page("HapaKristin"),
        Page("Not in a section", in_section=False),
        Page("https://teachablemachine.withgoogle.com/models/Y44cpwtyV/", "AI Personal"),
        Page("Community"),
        Page("Notice")    
    ]
)
