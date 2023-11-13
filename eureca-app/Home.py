import streamlit as st

#타이틀 & 이모티콘
st.markdown("<h1 style='text-align: center;'>☃️Lens in Gray☃️</h1>", unsafe_allow_html=True)

#구분선
st.divider()

#일반 글씨
st.write("Team 6 : uquahanuqui :christmas_tree:")

#이미지 첨부
img_url = "https://fimg5.pann.com/new/download.jsp?FileID=65745091"

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

#눈내림
st.snow()

#검색창
st.markdown("---")
search_query = st.text_input("Search :mag:")
