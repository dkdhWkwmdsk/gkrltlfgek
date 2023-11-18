
# gggg.py
import streamlit as st
import pandas as pd
st.title('Baeks Portfolio')
tab1, tab2, tab3, tab4 = st.tabs(["Home", "About me","Projects","Career"])
with tab1:
   st.header("Titanic Dataset")
   df=pd.read_csv("2023-11-18T01-14_export.csv")
   st.dataframe(df)
   st.divider()
   tab,tab2,tab3=st.tabs(["Sex","Pclass","Embarked"])
   with tab1:
      st.bar_chart(df,x="Sex",y="Pclass")
