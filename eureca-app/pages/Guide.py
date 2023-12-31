import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>Guide</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#내용
st.markdown("<p style='font-size: 22px; font-weight: bold;'>회원가입 안내</p>", unsafe_allow_html=True)
st.write(" ")

#회원가입 사진
img_url = "https://pbs.twimg.com/media/F_shmYmbgAAa4ft?format=jpg&name=large"

# 이미지를 중앙에 위치시키기 위한 CSS 스타일
centered_image_style = """
    display: flex;
    justify-content: center;
    align-items: center;
    height: 400px; /* 이미지 높이 조절 */
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
st.write("학생증 디자인의 회원가입 페이지를 통해 Lens in Gray의 일원이 되어 다양한 회원 혜택을 경험해 보세요.")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown("<p style='font-size: 22px; font-weight: bold;'>주문 안내</p>", unsafe_allow_html=True)
st.write(" ")
st.write("상품 주문은 다음 단계로 이루어집니다.")
st.write(" ")
st.write("- Step1: 상품 검색 혹은 추천")
st.write("- Step2: 장바구니에 담기")
st.write("- Step3: 회원 ID 로그인 또는 비회원 주문")
st.write("- Step4: 주문서 작성")
st.write("- Step5: 결제방법 선택 및 결제")
st.write("- Step6: 주문 성공 화면 (주문번호, 픽업 장소)")
st.write(" ")
st.write("비회원 주문 인경우 6단계에서 주문번호와 승인번호(카드 결제 시)를 꼭 메모해 두시기 바랍니다.")
st.write("단, 회원인 경우 자동 저장되므로 따로 관리하실 필요가 없습니다.")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown("<p style='font-size: 22px; font-weight: bold;'>결제 안내</p>", unsafe_allow_html=True)
st.write(" ")
st.write("고액 결제의 경우 안전을 위해 카드사에서 확인 전화를 드릴 수도 있습니다.")
st.write("확인 과정에서 도난 카드의 사용이나 타인 명의의 주문 등 정상적인 주문이 아니라고 판단될 경우 임의로 주문을 보류 또는 취소할 수 있습니다.")
st.write(" ")
st.write("무통장 입금은 상품 구매 대금은 PC 뱅킹, 인터넷뱅킹, 텔레뱅킹 혹은 가까운 은행에서 직접 입금하시면 됩니다.")
st.write("주문 시 입력한 입금자명과 실제 입금자의 성명이 반드시 일치하여야 하며, 7일 이내로 입금을 하셔야 하며 입금되지 않은 주문은 자동 취소됩니다.")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown("<p style='font-size: 22px; font-weight: bold;'>픽업 및 수령 안내</p>", unsafe_allow_html=True)
st.write(" ")
st.write("픽업 및 수령방법 : 도보 혹은 차량")
st.write("픽업 및 수령지역 : 본인 설정 주소지 근처 지역")
st.write("픽업 및 수령기간 : 픽업 및 수령 완료 안내 문자로부터 일주일")
st.write("픽업 및 수령안내 :")
st.write("픽업 및 수령 완료 안내 문자로 부터 일주일이 지나도 픽업하지 않으시는 경우 자동 픽업 취소됩니다.")
st.write("고객님께서 주문하신 상품은 입금 확인 후 픽업 장소를 안내해 드립니다. 다만, 상품 종류에 따라서 상품의 픽업 안내가 다소 지연될 수 있습니다.")
st.write(" ")
st.write("✲ 렌즈는 의료기기입니다. 구입하실 때에는 반드시 의사나 안경사의 처방에 근거해 구입하시기 바랍니다. 이에 택배로 상품을 수령하실 수 없는 점 양해 부탁드립니다.")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown("<p style='font-size: 22px; font-weight: bold;'>교환/반품 안내</p>", unsafe_allow_html=True)
st.write(" ")
st.write("교환 및 반품 방법")
st.write(" ")
st.write("상품 수령 후 되도록이면 24시간 안에 카카오톡 채널 또는 QnA 게시판에 접수 부탁드립니다.")
st.write("Lens in Gray 측에서 렌즈사에 교환/반품 신청을 진행합니다.")
st.write("접수 후 1-2일 이내 고객님께서 렌즈사에 방문하여 상품을 회수합니다.")
st.write("교환 및 반품의 경우 수령일로부터 7일 이내에 상품 회수가 완료되어야 합니다.")
st.write("불량으로 인한 교환 및 반품의 경우 Lens in Gray 측에서 추가 비용을 부담합니다.")
st.write(" ")
st.write("✲ 렌즈의 경우 의료기기로 분류되기 때문에 택배로 교환/반품할 수 없는 점을 양해 부탁드립니다.")
st.write(" ")
st.write(" ")
st.write("교환 및 반품이 불가능한 경우")
st.write(" ")
st.write("- 사용 흔적이 있는 경우 (개봉 및 오염 및 훼손 등)")
st.write("- 상품의 구성품을 훼손하거나 분실한 경우")
st.write("- 사전 접수 없이 상품을 임의로 반송했을 경우")
st.write("- 교환 가능 시기(제품 수령일로부터 7일)을 경과한 경우")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown("<p style='font-size: 22px; font-weight: bold;'>환불 안내</p>", unsafe_allow_html=True)
st.write(" ")
st.write("환불 시 반품 확인 여부를 확인한 후 3 영업일 이내에 결제 금액을 환불해 드립니다.")
st.write("신용카드로 결제하신 경우는 신용카드 승인을 취소하여 결제 대금이 청구되지 않게 합니다.")
st.write("(단, 신용카드 결제 일자에 맞추어 대금이 청구 될 수 있으면 이 경우 익월 신용카드 대금 청구 시 카드사에서 환급 처리됩니다.)")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown("<p style='font-size: 22px; font-weight: bold;'>기타 안내</p>", unsafe_allow_html=True)
st.write(" ")
st.write("- 렌즈는 의료기기입니다. 구입하실 때에는 반드시 의사나 안경사의 처방에 근거해 구입하시기 바랍니다.")
st.write("- 신규 가입 시 적립금 1,000원이 지급됩니다.")
st.write("- 적립금은 구매 금액, 할인 여부와 상관없이 사용 가능합니다.")
st.write("- 30자 이상의 텍스트 리뷰 작성 시 1,000원의 적립금이 지급됩니다.")
st.write("- 직접 촬영한 사진과 함께 30자 이상의 포토리뷰 작성 시 2,000원의 적립금이 지급됩니다.")
st.write("- 상품 구매 시 결제방법에 따라 적립금이 지급됩니다. (무통장 입금 2.5%, 카드 결제 1%, 실시간 계좌이체 0.5%)")
st.write("- 리뷰 작성 기한은 구매 후 한 달로 설정된 점 참고 부탁합니다.")

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

