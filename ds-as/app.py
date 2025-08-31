import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 페이지 설정을 넓은 레이아웃으로 변경합니다.
st.set_page_config(layout="wide")

# --- 앱 디자인을 위한 커스텀 CSS ---
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;600;700&family=Orbitron:wght@900&display=swap');

/* 타이틀 스타일링 */
h1 {
    font-family: 'Orbitron', sans-serif !important;
    color: #a5b4fc !important; /* Indigo color */
    text-shadow: 2px 2px 8px rgba(165, 180, 252, 0.5);
    font-size: 3rem !important;
}

/* 본문 및 탭 폰트 스타일링 */
.stMarkdown, .stTabs, .stHeader {
    font-family: 'IBM Plex Sans KR', sans-serif;
}

/* 탭 디자인 커스터마이징 */
.stTabs [data-baseweb="tab-list"] {
    gap: 24px;
}

.stTabs [data-baseweb="tab"] {
    height: 50px;
    white-space: pre-wrap;
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 8px 8px 0 0;
    transition: all 0.2s ease-in-out;
    border: 1px solid #4b5563;
}

.stTabs [data-baseweb="tab"]:hover {
    background-color: rgba(165, 180, 252, 0.1);
    border-bottom-color: #a5b4fc;
}

.stTabs [aria-selected="true"] {
    background-color: #4f46e5; /* Indigo-600 */
    border-color: #6366f1;
    color: white;
}

/* 탭 내부 헤더 스타일 */
h2 {
    border-left: 5px solid #6366f1;
    padding-left: 15px;
    color: #e0e7ff;
}
"""
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)


# 페이지 제목과 설명을 업데이트합니다.
st.title("🚀 ALGORITHM LAB")
st.markdown("### 시각적 도구를 통해 **정렬, 탐색, 해싱** 알고리즘의 세계를 탐험하세요!")

# 두 개의 학습 콘텐츠를 위한 탭을 생성합니다.
tab1, tab2 = st.tabs(["👾효율적인 알고리즘", "✅ [수행평가] 탐색 & 해싱 알고리즘 챌린지"])

# 첫 번째 탭: 기존의 정렬 알고리즘 시각화 (index.html)
with tab1:
    st.header("👾효율적인 알고리즘")
    
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
    st.header("✅ [수행평가] 탐색 & 해싱 알고리즘 챌린지")

    # index2.html 파일 경로 설정
    filepath2 = os.path.join(os.path.dirname(__file__), "htmls", "index2.html")
    
    # HTML 파일을 읽어와서 표시합니다.
    try:
        with open(filepath2, 'r', encoding='utf-8') as f:
            html_code2 = f.read()
            components.html(html_code2, height=1500, scrolling=True)
    except FileNotFoundError:
        st.error("오류: 'htmls/index2.html' 파일을 찾을 수 없습니다. 새로 생성된 HTML 파일을 해당 경로에 저장해주세요.")

