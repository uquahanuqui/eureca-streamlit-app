
import streamlit as st
import pandas as pd

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>Shop</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#메뉴
category = st.sidebar.selectbox("Shop", ["Lens-me", "O-lens", "Idol-lens", "HapaKristin"])

# 각 카테고리에 대한 페이지를 표시
if category == "Lens-me":
    st.write("Lens-me")
    st.link_button("Lens-me", "https://www.lens-me.com/shop/")

elif category == "O-lens":
    st.write("O-lens")
    st.link_button("O-lens", "https://o-lens.com/")

elif category == "Idol-lens":
    st.write("Idol-lens")
    st.link_button("Idol-lens", "https://www.i-dol.kr/")

elif category == "HapaKristin":
    st.write("HapaKristin")
    st.link_button("HapaKristin", "https://hapakristin.co.kr/")


import streamlit as st
import pandas as pd

# 데이터를 DataFrame으로 변환
data = {
    "Product Name": ["빅글로이 모카브라운", "빅글로이 헤이즐", "샤인터치 밀키 브라운", "샤인터치 밀키 그레이", "샤인터치 밀키 초코", 
                    "퓨어틴 브라운", "퓨어틴 초코", "글로이 내츄럴 라떼브라운", "글로이 내츄럴 모카브라운", "더블틴트 그레이"],
    "Description": ["13.6mm (1Month 권장)", "13.6mm (1Month 권장)", "12.7mm (1Month 권장)", "12.7mm (1Month 권장)", 
                    "12.7mm (1Month 권장)", "12.8mm (1Month 권장)", "12.8mm (1Month 권장)", "13.0mm (1Month 권장)", 
                    "13.0mm (1Month 권장)", "12.9mm (1Month 권장)"]
}

df = pd.DataFrame(data)
print(df)




















# 스트림릿 타이틀 설정
st.title('제품 목록')

# 데이터를 테이블로 표시
st.table(df)




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
