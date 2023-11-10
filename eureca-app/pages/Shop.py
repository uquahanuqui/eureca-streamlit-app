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


import pandas as pd
import streamlit as st

# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [퓨어비전2 멀티포컬
바이오피니티 토릭
에어옵틱스 토릭
나이트앤데이
울트라 토릭
바이오피니티
퓨어비전2
옵티마 FW
울트라
],
            "second column": [10, 20, 30, 40],
        }
    )

# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# Display the dataframe and allow the user to stretch the dataframe
# across the full width of the container, based on the checkbox value
st.dataframe(df, use_container_width=st.session_state.use_container_width)


    

