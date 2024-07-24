import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize-matplotlib

# CSV 파일 경로
file_path = '202406_202406_연령별인구현황_월간 (1).csv'

# 데이터 로드
@st.cache
def load_data():
    return pd.read_csv(file_path, encoding='euc-kr')

data = load_data()

# Streamlit 애플리케이션 타이틀
st.title('지역별 중학생 인구 비율')

# 사용자로부터 지역 입력 받기
region = st.text_input('지역을 입력하세요:', '서울특별시')

# 해당 지역 데이터 필터링
region_data = data[data['행정구역'].str.contains(region)]

if not region_data.empty:
    total_population = int(region_data['2024년06월_계_총인구수'].iloc[0].replace(',', ''))
    mid_school_population = int(region_data['2024년06월_계_10~19세'].iloc[0].replace(',', ''))
    
    # 원 그래프 데이터
    sizes = [mid_school_population, total_population - mid_school_population]
    labels = ['중학생 인구 (10~19세)', '기타 인구']
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # 중학생 인구 비율을 강조
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # 원을 원형으로 그림
    
    st.pyplot(fig1)
else:
    st.write('입력하신 지역의 데이터가 없습니다.')
