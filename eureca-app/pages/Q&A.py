import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>Q&A</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#글씨
st.markdown("<p style='font-size: 27px; font-weight: bold; margin: 0px 0;'>FAQ</p>", unsafe_allow_html=True)
st.markdown("---")
st.write("Q. 실시간 문의가 가능한가요?")
st.write("Q. AI Personal 추천이 정확한가요?")
st.write("Q. 오프라인 쇼룸이 있나요?")

st.markdown("---")
st.markdown("<p style='font-size: 27px; font-weight: bold; margin: 0px 0;'>Q&A</p>", unsafe_allow_html=True)
st.markdown("---")
st.write("‣ 주문 문의 :lock:")
st.caption("→ RE: 주문 문의 :lock:")
st.write("‣ 기타 문의 :lock:")
st.caption("→ RE: 기타 문의 :lock:")
st.write("‣ 상품 문의 :lock:")
st.caption("→ RE: 상품 문의 :lock:")

#
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.markdown("<h1 style='text-align: center;'>❄️❄️❄️</h1>", unsafe_allow_html=True)
st.write(" ")
st.write(" ")

#프로필
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.write("<div style='display: flex; margin-left: 220px;'><a href='https://www.lens-me.com/shop/' style='font-size: 14px; text-align: center; color: black;'>INSTAGRAM</a></div>", unsafe_allow_html=True)

with col2:
    st.write("<div style='display: flex; justify-content: center; margin-left: -25px;'><a href='https://o-lens.com/' style='font-size: 14px; text-align: center; color: black;'>BLOG</a></div>", unsafe_allow_html=True)

with col3:
    st.write("<div style='display: flex; margin-left: -95px;'><a href='http://pf.kakao.com/_HBxnbG' style='font-size: 14px; text-align: center; color: black;'>KAKAO CHANNEL</a></div>", unsafe_allow_html=True)
    
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

