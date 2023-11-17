
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

# Image URLs
image_urls = [
    "https://file.o-lens.com/prd_img/20670/547bb379-1c08-46f8-b77b-bb7428153d45%ED%93%A8%EC%96%B4%ED%8B%B4_SUM_ch.jpg?w=330",
    "https://file.o-lens.com/prd_img/20670/dde68f3a-dc5b-4ada-8782-6f8bfe2afbc0%ED%93%A8%EC%96%B4%ED%8B%B4_L_ch.png?w=90",
    "https://file.o-lens.com/prd_img/20650/672c9c08-e8f3-425a-ba93-bc8275381bdcSUM_%EB%9D%BC%EB%96%BC%EB%B8%8C%EB%9D%BC%EC%9A%B4.jpg?w=330",
    "https://file.o-lens.com/prd_img/20650/7acdde5c-7224-4695-aa4e-ee805e259efbL_%EB%9D%BC%EB%96%BC%EB%B8%8C%EB%9D%BC%EC%9A%B4.png?w=90",
    "https://file.o-lens.com/prd_img/20651/7aeb28d8-746b-4008-a6b8-87b8ce3972acSUM_%EB%AA%A8%EC%B9%B4%EB%B8%8C%EB%9D%BC%EC%9A%B4.jpg?w=330",
    "https://file.o-lens.com/prd_img/20651/b464f894-2efa-43c2-8be0-1230eb41cf21L_%EB%AA%A8%EC%B9%B4%EB%B8%8C%EB%9D%BC%EC%9A%B4.png?w=90"
]

# Product name and diameter data
data = {
    "products__product-name": [
        "Big Gloy Mocha Brown",
        "Big Gloy Hazel",
        "Shine Touch Milky Brown",
        "Shine Touch Milky Gray",
        "Shine Touch Milky Choco",
        "Puretin Brown",
        "Puretin Chocolate",
        "Gloy Natural Latte Brown",
        "Gloy Natural Mocha Brown",
        "Double Tint Gray",
        "Double Tint Brown",
        "French Shine Hazel",
        "French Shine Gray",
        "Jennifer 3-Con Olive",
        "Jennifer 3 Con Gray",
        "Jennifer 3 Con Hazel",
        "Plum chocolate",
        "Coming Chocolate",
        "And Black",
        "Neil's Gray",
        "Neil's Brown",
        "Rowling Gray",
        "Rowling Brown",
        "Moodnight Mood Gray",
        "Moodnight Mood Brown",
        "Wannabe Camel Brown",
        "Wannabe Humming Brown",
        "Bibeering Brown",
        "Symphony 3-Con Hazel",
        "Bea-ring Gray",
        "Symphony 3-con Gray",
        "Bibi ring chocolate",
        "It's chocolate",
        "It's Black",
        "Symphony 3-Con Green",
        "Bibi ring pink",
        "Gloy Brown",
        "Bibi 3 Con Brown",
        "Beeping Beige",
        "Skandi Hazel"
    ],
    "products__product-desc": [
        "13.6 mm (1Month recommended)",
        "13.6 mm (1Month recommended)",
        "12.7 mm (1 Month Recommended)",
        "12.7 mm (1 Month Recommended)",
        "12.7mm (1Month recommended)",
        "12.8 mm (1Month recommended)",
        "12.8mm (1Month recommended)",
        "13.0 mm (1 Month Recommended)",
        "13.0 mm (1 Month Recommended)",
        "12.9 mm (1Month recommended)",
        "12.9 mm (1Month recommended)",
        "13.2 mm (1 Month Recommended)",
        "13.2 mm (1Month recommended)",
        "13.3 mm (1 Month Recommended)",
        "13.3 mm (1Month recommended)",
        "13.3 mm (1 Month Recommended)",
        "13.2 mm (1 Month recommended)",
        "13.8 mm (1 Month recommended)",
        "13.3 mm (1 Month recommended)",
        "13.5 mm (1 Month Recommended)",
        "13.5 mm (1 Month Recommended)",
        "12.5 mm (1 Month Recommended)",
        "12.5 mm (1 Month Recommended)",
        "13.3 mm (1 Month recommended)",
        "13.3 mm (1 Month recommended)",
        "13.3 mm (1 Month Recommended)",
        "13.0 mm (1 Month Recommended)",
        "13.0 mm (1Month recommended)",
        "13.0 mm (1 Month recommended)",
        "13.5 mm (1 Month Recommended)",
        "13.0 mm (1Month recommended)",
        "13.5 mm (1 Month Recommended)",
        "13.0mm (1Month recommended)",
        "12.9mm (1Month recommended)",
        "13.1 mm (1Month recommended)",
        "13.5 mm (1 Month Recommended)",
        "13.0 mm (1Month recommended)",
        "13.1 mm (1 Month Recommended)",
        "13.8 mm (1Month recommended)",
        "13.0 mm (1 Month recommended)",
        "11.9 mm (1 Month Recommended)"
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
st.dataframe(df)




















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
