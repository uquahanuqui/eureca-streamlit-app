import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>☃️Lens in Gray☃️</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#일반 글씨
st.write("Team 6 : uquahanuqui :christmas_tree:")

#이미지 첨부
img_url = "http://www.dizzotv.com/site/data/img_dir/2022/07/21/2022072180056_0.jpg"

# 이미지를 중앙에 위치시키기 위한 CSS 스타일
centered_image_style = """
    display: flex;
    justify-content: center;
    align-items: center;
    height: 400px; /* 이미지 높이 조절 */
"""

# 이미지를 스타일링하여 중앙에 표시
st.markdown(
    f'<div style="{centered_image_style}">'
    f'<img src="{img_url}" alt="Image" style="max-width: 100%; max-height: 100%;">'
    '</div>',
    unsafe_allow_html=True
)

#눈내림
st.snow()

#검색창
st.markdown("---")
search_query = st.text_input("Search :mag:")

#프로필
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.write("<div style='display: flex; margin-left: 220px;'><a href='https://www.lens-me.com/shop/' style='font-size: 14px; text-align: center; color: black;'>INSTAGRAM</a></div>", unsafe_allow_html=True)

with col2:
    st.write("<div style='display: flex; justify-content: center; margin-left: -25px;'><a href='https://o-lens.com/' style='font-size: 14px; text-align: center; color: black;'>BLOG</a></div>", unsafe_allow_html=True)

with col3:
    st.write("<div style='display: flex; margin-left: -95px;'><a href='https://www.i-dol.kr/' style='font-size: 14px; text-align: center; color: black;'>KAKAO CHANNEL</a></div>", unsafe_allow_html=True)
    
st.write(" ")
st.write("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 15px;'>Lens in Gray</span> <span style='font-size: 15px;'>Co.</span> <span style='font-size: 12px;'>Owner</span> <span style='font-size: 15px;'>Uquahanuqui</span> </p>", unsafe_allow_html=True)
st.write("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 12px;'>Business Number</span> <span style='font-size: 15px;'>20230922</span> </p>", unsafe_allow_html=True)
st.write(" ")
st.write("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 15px;'>CUSTOMER CARE</span></p>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 14px;'>Phone</span> <span style='margin-right: 7px;'> </span> <span style='font-size: 14px;'>+82 10-4536-6713</span></p>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 14px;'>Email</span> <span style='margin-right: 7px;'> </span> <span style='font-size: 14px;'>hyb0320@kookmin.ac.kr</span></p>", unsafe_allow_html=True)
st.write(" ")
st.write("<p style='text-align: center; margin: 5px; line-height: 0.8;'><span style='font-size: 15px;'>OFFICE</span></p>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; margin: 5px; line-height: 0.8;'>#77 Kookmin University Management Hall, Jeongneung-ro, Seongbuk-gu, Seoul</p>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; margin: 5px; line-height: 0.8;'>서울특별시 성북구 정릉로 77 국민대학교 경영관 (02707)</p>", unsafe_allow_html=True)
st.divider()
