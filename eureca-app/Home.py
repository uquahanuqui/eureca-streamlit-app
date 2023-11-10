import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>Lens in Gray</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#일반 글씨
st.markdown("<h1 style='text-align: center;'>☃️</h1>", unsafe_allow_html=True)
st.write("Team 6 : uquahanuqui :christmas_tree:")

#눈내림
st.snow()

#검색창
st.markdown("---")
search_query = st.text_input("Search :mag:")
