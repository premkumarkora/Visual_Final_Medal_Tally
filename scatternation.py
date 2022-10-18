import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.medals_long()
st.set_page_config(
    page_title="Counties & Medals",
    page_icon="✅",
    layout="wide",
)

st.markdown('<div style="text-align: center;"><h1>Final Medal Tally</H1></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center;"><p>If you observe carefully the two graphs has different X and Y elements from the same table</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.write(df)
with col2:
    barfig = px.bar(data_frame=df, x="nation", y="count", color="medal", width=300, height=300)
    st.plotly_chart(barfig)
with col3:
    scatterfig = px.scatter(data_frame=df, x="count", y="nation", color="medal", symbol="medal", width=300, height=300)
    st.plotly_chart(scatterfig)


