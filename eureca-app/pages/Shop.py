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


# 스트림릿 타이틀 설정
st.title('제품 목록')

# 데이터를 테이블로 표시
st.table(df)




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
