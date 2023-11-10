import streamlit as st

#타이틀 & 이모티콘
st.title("Shop select")

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

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

pip install streamlit pandas

import streamlit as st
import pandas as pd

file = st.file_uploader("파일을 선택하세요.", type=['xlsx'])
    if uploaded_file:
        df = pd.read_excel(file)
        st.dataframe(df)


    

