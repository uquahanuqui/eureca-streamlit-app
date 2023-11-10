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



    

