import streamlit as st
from PIL import Image
import requests
import json  # json 모듈 추가
from io import BytesIO

# 타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>AI Personal</h1>", unsafe_allow_html=True)

# 구분선
st.divider()

# 링크 버튼
st.link_button("카카오 채널", "http://pf.kakao.com/_xblxexjG")
st.link_button("채팅 바로가기", "http://pf.kakao.com/_xblxexjG/chat")

# 스트림릿 앱 제목
st.title("Teachable Machine Image Classification")

# 이미지 업로드
uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])

# 이미지 예측 함수
def predict_image(image):
    # Teachable Machine 모델 API 엔드포인트
    model_api = "https://teachablemachine.withgoogle.com/models/Y44cpwtyV"
    
    # 이미지를 바이너리 데이터로 변환
    img_data = BytesIO()
    image.save(img_data, format="JPEG")
    img_data = img_data.getvalue()
    
    # 이미지 분류를 위한 POST 요청
    response = requests.post(model_api, files={"file": ("image.jpg", img_data, "image/jpeg")})
    
    try:
        # JSON 데이터 파싱
        prediction = response.json()
    except json.decoder.JSONDecodeError as e:
        st.error("An error occurred while decoding the JSON response.")
        st.error(f"Error Message: {str(e)}")
        prediction = {}  # 빈 딕셔너리 또는 오류 처리에 맞는 다른 값을 사용할 수 있습니다.
    
    return prediction

# 이미지 업로드 및 예측
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    
    # 예측 수행
    predictions = predict_image(image)
    
    # 예측 결과 표시
    st.subheader("Prediction Results")
    
    for class_name, score in predictions.items():
        st.write(f"{class_name}: {score:.4f}")

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
