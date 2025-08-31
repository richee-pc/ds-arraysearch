import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 페이지 설정을 넓은 레이아웃으로 변경합니다.
st.set_page_config(layout="wide")

# 페이지 제목과 설명을 업데이트합니다.
st.title("🚀 인터랙티브 알고리즘 학습")
st.markdown("다양한 알고리즘을 시각적으로 체험하며 학습해보세요! 각 탭을 클릭하여 원하는 콘텐츠를 확인하세요.")

# 두 개의 학습 콘텐츠를 위한 탭을 생성합니다.
tab1, tab2 = st.tabs(["정렬 알고리즘 시각화", "탐색 & 해싱 알고리즘 챌린지"])

# 첫 번째 탭: 기존의 정렬 알고리즘 시각화 (index.html)
with tab1:
    st.header("정렬 알고리즘 시각화 도구")
    
    # index.html 파일 경로 설정
    filepath1 = os.path.join(os.path.dirname(__file__), "htmls", "index.html")

    # HTML 파일을 읽어와서 표시합니다.
    try:
        with open(filepath1, 'r', encoding='utf-8') as f:
            html_code1 = f.read()
            components.html(html_code1, height=1500, scrolling=True)
    except FileNotFoundError:
        st.error("오류: 'htmls/index.html' 파일을 찾을 수 없습니다. 경로를 확인해주세요.")

# 두 번째 탭: 새로운 탐색 & 해싱 알고리즘 챌린지 (index2.html)
with tab2:
    st.header("탐색 & 해싱 알고리즘 탐구 챌린지")

    # index2.html 파일 경로 설정
    filepath2 = os.path.join(os.path.dirname(__file__), "htmls", "index2.html")
    
    # HTML 파일을 읽어와서 표시합니다.
    try:
        with open(filepath2, 'r', encoding='utf-8') as f:
            html_code2 = f.read()
            components.html(html_code2, height=1500, scrolling=True)
    except FileNotFoundError:
        st.error("오류: 'htmls/index2.html' 파일을 찾을 수 없습니다. 새로 생성된 HTML 파일을 해당 경로에 저장해주세요.")
