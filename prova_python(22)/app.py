import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Índice de Qualidade de Vida Urbana", page_icon="📊", layout="wide")

df = pd.read_csv("bd_iqvu_1994_2016.csv", sep=";", encoding="latin-1",
decimal=",")
df.columns = df.columns.str.replace("\ufeff", "", regex=False).str.strip()

df_filtrado = df[
    (df["NOMEUP"].isin(["Taquaril", "Santa Ines"])) &
    (df["SERIE"] == "SERIE HISTORICA")
].copy()

st.title("IQVU")
st.header("v^v^v^v^v^v^v^v^-༺❀༻-^v^v^v^v^v^v^v^v")
st.caption("Índice de Qualidade de Vida Urbana dos bairros de Belo Horizonte | Fonte: Prefeitura de Belo Horizonte")
    
df_taquaril = df_filtrado[df_filtrado["NOMEUP"] == "Taquaril"] 
 
fig_linha_taquaril = px.line( 
    df_taquaril, 
    x="ANO", 
    y="IQVU", 
    markers=True, 
    title="Evolução do IQVU — Taquaril (1994 a 2016)", 
    template="plotly_dark" 
) 
fig_linha_taquaril.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8) 
fig_linha_taquaril.update_xaxes(type="category") 
st.plotly_chart(fig_linha_taquaril, use_container_width=True)

df_santa_ines = df_filtrado[df_filtrado["NOMEUP"] == "Santa Ines"] 
 
fig_linha_santa_ines = px.line( 
    df_santa_ines, 
    x="ANO", 
    y="IQVU", 
    markers=True, 
    title="Evolução do IQVU — Santa Inês (1994 a 2016)", 
    template="plotly_dark" 
) 
fig_linha_santa_ines.update_traces(line_color="#00F5D4", line_width=3, marker_size=8) 
fig_linha_santa_ines.update_xaxes(type="category") 
st.plotly_chart(fig_linha_santa_ines, use_container_width=True)


with st.sidebar:
    st.header("Filtros")
    Escolha = st.selectbox("Tabela", list("12"))