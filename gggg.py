import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title("Iris 데이터셋 시각화")

    # Iris 데이터셋 로드
    iris_df = load_iris_dataset()

    # 사용자로부터 꽃 종류 선택
    selected_species = st.selectbox("꽃 종류 선택", iris_df['species'].unique())

    # 선택한 꽃 종류의 데이터 필터링
    selected_data = iris_df[iris_df['species'] == selected_species]

    # 선택한 꽃 종류의 특성 시각화
    visualize_data(selected_data)

def load_iris_dataset():
    # seaborn의 Iris 데이터셋 로드
    iris = sns.load_dataset('iris')
    return iris

def visualize_data(data):
    # 꽃 종류에 따른 특성 시각화
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # 꽃받침 길이와 꽃받침 너비의 관계
    sns.scatterplot(x='sepal_length', y='sepal_width', data=data, hue='species', ax=ax1)
    ax1.set_title('Sepal Length vs Sepal Width')

    # 꽃잎 길이와 꽃잎 너비의 관계
    sns.scatterplot(x='petal_length', y='petal_width', data=data, hue='species', ax=ax2)
    ax2.set_title('Petal Length vs Petal Width')

    st.pyplot(fig)

if __name__ == "__main__":
    main()
