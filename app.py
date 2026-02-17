import streamlit as st
import pandas as pd
import plotly_express as px
df = pd.read_csv('vehicles.csv')
print(df.head(4))
st.header('Bemvindo ao meu projecto Sprint 5')
hist_button = st.checkbox('Criar Histograma (Plotly_Express)')
px_button = st.checkbox('Criar Gráfico Dispersão')
if hist_button:
    st.write('Criando um histograma para o conjunto de dados')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)
if px_button:
    st.write('Criando um gráfico de dispersão do conjunto de dados')
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
