
# gggg.py
import streamlit as st
import pandas as pd

def main():
    st.title("간단한 데이터 시각화 애플리케이션")

    # CSV 파일 업로드
    uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

    if uploaded_file is not None:
        # 업로드된 파일을 DataFrame으로 읽기
        df = pd.read_csv(uploaded_file)

        # 데이터 테이블 표시
        st.dataframe(df)

        # 사용자로부터 선택한 컬럼
        selected_column = st.selectbox("시각화할 컬럼 선택", df.columns)

        # 선택한 컬럼의 히스토그램
        st.pyplot(plot_histogram(df, selected_column))

def plot_histogram(df, column):
    # 선택한 컬럼의 히스토그램 생성
    fig, ax = plt.subplots()
    df[column].hist(ax=ax, bins=20, edgecolor='black')
    ax.set_title(f'{column} Histogram')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    return fig

if __name__ == "__main__":
    main()
