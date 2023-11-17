import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>Q&A</h1>", unsafe_allow_html=True)

#안내
st.markdown("---", unsafe_allow_html=True)
st.markdown("<p style='margin: 0px;'>Call 82+10 4536 6713 (11:00 ~ 17:00 / 13:00 ~ 14:00 점심시간)</p>", unsafe_allow_html=True)
st.markdown("<p style='margin: 0px;'>Email hyb0320@kookmin.ac.kr</p>", unsafe_allow_html=True)
st.markdown("<p style='margin: 0px;'>Kakaotalk 11:00 ~ 17:00 (13:00 ~ 14:00 점심시간)</p>", unsafe_allow_html=True)

#구분선
st.divider()

#글씨
st.markdown("<p style='font-size: 27px; font-weight: bold; margin: 0px 0;'>FAQ</p>", unsafe_allow_html=True)
st.markdown("---")
with st.expander("Q. 실시간 문의가 가능한가요?"):
    st.write("렌즈 인 그레이 카카오톡 채널을 통해 실시간 상담원 연결이 가능합니다. 
    월~금 11:00~17:00
    점심시간 : 12:00~13:00
    * 주말 및 공휴일 제외
    * 업무시간 외에 전송된 메세지는 전달되지 않습니다. 이 경우 1:1 QnA 게시판을 통해 문의 부탁드립니다.")
with st.expander("Q.  AI Personal 추천이 정확한가요?"):
    st.write("이 칸은 기본적으로 접혀있습니다.")
with st.expander("Q. 오프라인 쇼룸이 있나요?"):
    st.write("렌즈 인 그레이는 아직 오프라인 쇼룸을 운영하지 않고 있습니다. 오프라인에도 제품들을 만나보실 수 있도록 부지런히 노력하도록 하겠습니다.")

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

