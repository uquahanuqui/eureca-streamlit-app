import streamlit as st
import pandas as pd

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



st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, column_order=None, column_config=None)
st.dataframe("https://www.lens-me.com/shop/goods_detail.php?ps_uid=66178","https://image.bmit.co.kr/lens-me.com/upload/goods/2023090412044143512/2023090412044143512_0_400.jpg","https://image.bmit.co.kr/lens-me.com/upload/goods/2023090412044143512/2023090412044143512_1_400.jpg","유스 쵸코","13.0mm","25,000","1+1")


    

