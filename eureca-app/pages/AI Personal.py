import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>AI Personal</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#링크 버튼
st.link_button("카카오 채널", "http://pf.kakao.com/_HBxnbG")
st.link_button("채팅 바로가기", "http://pf.kakao.com/_HBxnbG/chat")

#프로필
# 전체 배경색을 흰색으로 설정
st.write("""
<style>
    body {
        background-color: white;
    }
    .stApp {
        display: flex;
        justify-content: space-around;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background-color: transparent;
        padding: 10px 0;
    }
    .btn-link {
        font-size: 14px;
        text-align: center;
        color: black;
        margin: 0 2px;  # 텍스트 간의 간격을 더욱 좁게 조절합니다.
        padding: 3px 5px;  # 버튼 주변의 여백을 조절합니다.
        text-decoration: none;  # 밑줄을 제거합니다.
    }
</style>
""", unsafe_allow_html=True)

# 세 개의 버튼 생성
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style="text-align: center;">
            <a href='https://www.instagram.com/lensingray.official/' 
               class='btn-link' style='color: black;'>
               INSTAGRAM
            </a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="text-align: center;">
            <a href='https://o-lens.com/' 
               class='btn-link' style='color: black;'>
               BLOG
            </a>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style="text-align: center;">
            <a href='http://pf.kakao.com/_HBxnbG' 
               class='btn-link' style='color: black;'>
               KAKAO CHANNEL
            </a>
        </div>
    """, unsafe_allow_html=True)

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

