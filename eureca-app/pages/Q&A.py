import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>Q&A</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#글씨
st.header("FAQ")
st.markdown("---")
st.write("Q. 실시간 문의가 가능한가요?")
st.write("Q. AI Personal 추천이 정확한가요?")
st.write("Q. 오프라인 쇼룸이 있나요?")

st.markdown("---")
st.header("Q&A")
st.markdown("---")
st.write("‣ 주문 문의 :lock:")
st.caption("→ RE: 주문 문의 :lock:")
st.write("‣ 기타 문의 :lock:")
st.caption("→ RE: 기타 문의 :lock:")
st.write("‣ 상품 문의 :lock:")
st.caption("→ RE: 상품 문의 :lock:")
