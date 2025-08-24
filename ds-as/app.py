import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 페이지 설정을 넓은 레이아웃으로 변경합니다.
st.set_page_config(layout="wide")

# 페이지 제목과 간단한 설명을 추가합니다.
st.title("🚀 인터랙티브 정렬 & 탐색 알고리즘 학습")
st.markdown("HTML, CSS, JavaScript로 제작된 시각화 도구를 Streamlit을 통해 배포합니다. 아래에서 다양한 알고리즘을 직접 체험해보세요!")

# 현재 작업 디렉토리를 기준으로 HTML 파일의 절대 경로를 생성합니다.
# 이 app.py 파일과 같은 위치에 'index.html' 파일이 있어야 합니다.
filepath = os.path.join(os.path.dirname(__file__), "./htmls/index.html")

# HTML 파일을 읽어옵니다.
try:
    with open(filepath, 'r', encoding='utf-8') as f:
        html_code = f.read()
        # Streamlit 앱에 HTML 컴포넌트를 삽입합니다.
        # height를 충분히 주어 스크롤바가 생기지 않도록 조정합니다.
        components.html(html_code, height=1500, scrolling=True)
except FileNotFoundError:
    st.error("오류: 'index.html' 파일을 찾을 수 없습니다. app.py와 같은 폴더에 저장해주세요.")

st.info("각 알고리즘 탭을 클릭하여 시뮬레이션을 시작할 수 있습니다.")