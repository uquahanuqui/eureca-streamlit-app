import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>About</h1>", unsafe_allow_html=True)

#구분선
st.divider()
st.write(" ")
st.write(" ")
st.write(" ")

#이미지 첨부
img_url = "https://i.pinimg.com/originals/a9/09/27/a9092792aa751e2d55d016693d9b5edd.jpg"

# 이미지를 중앙에 위치시키기 위한 CSS 스타일
centered_image_style = """
    display: flex;
    justify-content: center;
    align-items: center;
    height: 300px; /* 이미지 높이 조절 */
"""

# 이미지를 스타일링하여 중앙에 표시
st.markdown(
    f'<div style="{centered_image_style}">'
    f'<img src="{img_url}" alt="Image" style="max-width: 100%; max-height: 100%;">'
    '</div>',
    unsafe_allow_html=True
)

#내용
st.write(" ")
st.write(" ")
st.write(" ")
st.markdown("<p style='text-align: center;'line-height: 1.0;>Lens in Gray는 우리가 가장 나다울 수 있도록,</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'line-height: 1.0;>매번 렌즈를 사용할 때마다 자신의 컬러에 꼭 맞아 행복한 감정을 간직할 수 있도록,</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>좋은 서비스와 섬세한 추천을 제공합니다.</p>", unsafe_allow_html=True)
st.write(" ")
st.markdown("<p style='text-align: center;'>우리는 매년 다양한 렌즈사와 협업하여 다채로운 렌즈 추천을 선보이기도 하며</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>힘 주지 않아도 멋스럽고 편안한 착용감과 트렌드하고 깔끔한  Lens in Gray만의 감성을 추구합니다.</p>", unsafe_allow_html=True)
st.write(" ")
st.markdown("<p style='text-align: center;'>트렌드가 변할수록 더욱 빛을 발하는 가치가 되기를 소망합니다.</p>", unsafe_allow_html=True)
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

#내용(영어)
st.markdown("<p style='text-align: center;'>Lens in Gray makes us feel the most like me,</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>It provides good service and detailed recommendations so that</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>you can keep happy emotions that fit your color every time you use the lens.</p>", unsafe_allow_html=True)
st.write(" ")
st.markdown("<p style='text-align: center;'>We collaborate with various lens companies every year to present various lens recommendations</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>It pursues a cool and comfortable fit without giving it strength,</p>", unsafe_allow_html=True)
st.write(" ")
st.markdown("<p style='text-align: center;'>I hope that the more trends change, the more value it shines.</p>", unsafe_allow_html=True)

#
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.markdown("<h1 style='text-align: center;'>❄️❄️❄️</h1>", unsafe_allow_html=True)
st.write(" ")
st.write(" ")

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
    <a href='http://pf.kakao.com/_xblxexjG' 
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
