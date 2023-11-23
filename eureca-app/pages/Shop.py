import streamlit as st
import pandas as pd

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>Shop</h1>", unsafe_allow_html=True)

#구분선
st.divider()

import streamlit as st
import pandas as pd

def create_streamlit_app():
    # Title for the Streamlit app
    st.title("Product Table")

    # Data for the table
    data = [
    ("유스 원데이 블랙", "13.0mm", "18,000"),
    ("유스 원데이 쵸코", "13.0mm", "18,000"),
    ("유스 원데이 그레이", "13.0mm", "18,000"),
    ("오리지널 원데이 시리즈 베이블리 그레이(10P)", "13.4mm", "18,000"),
    ("악마 원데이 러버블 쵸코", "13.0mm", "55,000"),
    ("악마 원데이 러버블 그레이", "13.0mm", "55,000"),
    ("오리지널 원데이 시리즈 베이블리 브라운(10P)", "13.4mm", "18,000"),
    ("오리지널 원데이 시리즈 아이듀 톤업브라운(10P)", "13.0mm", "18,000"),
    ("메이크오버 원데이 베이블리 브라운(20P)", "13.4mm", "32,000"),
    ("악마 원데이 클로링 브라운", "13.2mm", "55,000"),
    ("악마 원데이 리얼핏 3칼라 브라운", "13.5mm", "55,000"),
    ("오리지널 원데이 시리즈 릴문스킨 브라운(10P)", "13.2mm", "18,000"),
    ("메이크오버 원데이 홀리브 브라운(20P)", "13.8mm", "32,000"),
    ("메이크오버 원데이 위키 브라운(20P)", "13.8mm", "32,000"),
    ("오리지널 원데이 시리즈 블론티 브라운(10P)", "13.3mm", "18,000"),
    ("오리지널 원데이 시리즈 아이듀 톤업브라운(30P)", "13.0mm", "36,000"),
    ("리얼썸 3칼라 원데이 브라운", "13.7mm", "36,000"),
    ("노블미스틱 원데이 리얼썸 브라운 (30p)", "12.9mm", "36,000"),
    ("악마 원데이 홀로리스 진저브라운", "13.2mm", "55,000"),
    ("메이크오버 원데이 위키 브라운(4P)", "13.8mm", "9,000")
]


    # Creating a DataFrame from the data
    df = pd.DataFrame(data, columns=["Product Name", "Lens Size", "Product Price"])

    # Displaying the DataFrame in the Streamlit app
    st.write(df)

# This line is necessary to run the app
if __name__ == '__main__':
    create_streamlit_app()










#프로필
st.markdown("---")
# 전체 배경색을 흰색으로 설정
st.write("""
<style>
    body {
        background-color: white;
    }
    .btn-container {
        display: flex;
        justify-content: center;  # 가운데 정렬
        align-items: center;  # 수직 가운데 정렬
        gap: 10px;  # 버튼간의 간격 조절
    }
    .btn-link {
        font-size: 14px;
        text-align: center;
        color: black !important;  # 글씨 색을 검정색으로 강제로 설정
        background-color: transparent;  # 배경색을 투명하게 설정
        border: 1px solid black;  # 테두리 추가
        padding: 5px 10px;  # 버튼 내 여백 조절
        text-decoration: none;  # 밑줄 제거
    }
</style>
""", unsafe_allow_html=True)

# 세 개의 버튼 생성 (버튼 텍스트 사이에 공백 추가)
st.markdown("""
<div class="btn-container">
    <a href='https://www.instagram.com/lensingray.official/' 
       class='btn-link'>INSTAGRAM</a>
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <a href='https://blog.naver.com/lens_in_gray' 
       class='btn-link'>BLOG</a>
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <span>&nbsp;</span>  <!-- 공백 추가 -->
    <a href='http://pf.kakao.com/_HBxnbG' 
       class='btn-link'>KAKAO CHANNEL</a>
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
