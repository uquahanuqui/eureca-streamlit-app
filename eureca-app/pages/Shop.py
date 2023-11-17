Section (name="Cool apps", icon=":pig:"),
Page ("example_app/example_four•py", "Example Four", "Ш"),
Page ("example_app/example_two.py", "Example Two", "")








import streamlit as st
import pandas as pd

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>Shop</h1>", unsafe_allow_html=True)

#구분선
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



import streamlit as st
import pandas as pd

def main():
    st.title('CSV 파일 업로드')

    # 파일 업로더 위젯을 만듭니다.
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=['csv'])

    if uploaded_file:
        # Pandas를 사용하여 CSV 파일을 데이터프레임으로 읽습니다.
        df = pd.read_csv(uploaded_file)

        # 데이터프레임을 스트림릿에 표시합니다.
        st.dataframe(df)

if __name__ == "__main__":
    main()


import streamlit as st
from PIL import Image

# 타이틀 설정
st.title('PNG 파일 뷰어')

# 파일 업로드 부분
uploaded_file = st.file_uploader("파일을 업로드하세요", type=['png'])

if uploaded_file is not None:
    # 파일을 읽고 이미지로 변환
    image = Image.open(uploaded_file)
    # 이미지 표시
    st.image(image, caption='업로드된 이미지', use_column_width=True)



import streamlit as st
from PIL import Image

# 타이틀 설정
st.title('WEBP 파일 뷰어')

# 파일 업로드 부분
uploaded_file = st.file_uploader("파일을 업로드하세요", type=['webp'])

if uploaded_file is not None:
    # 파일을 읽고 이미지로 변환
    image = Image.open(uploaded_file)
    # 이미지 표시
    st.image(image, caption='업로드된 이미지', use_column_width=True)




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



import streamlit as st

# 이미지 URL
image_url = "https://file.o-lens.com/prd_img/20672/a57f28ad-0b7a-494d-b7ba-e60ea9b5fb4b%EC%83%A4%EC%9D%B8%ED%84%B0%EC%B9%98_br_L.png?w=90"

# 이미지 표시
st.image(image_url, use_container_width=True)














# 스트림릿 타이틀 설정
st.title('제품 목록')

# 데이터를 테이블로 표시
st.table(df)




#프로필
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
    <a href='https://o-lens.com/' 
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
