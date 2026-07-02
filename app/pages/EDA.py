import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Análisis EDA Profundo", page_icon="📈", layout="wide")
st.title("📈 Análisis Exploratorio Avanzado (EDA)")
st.markdown("---")

ruta_datos = "data/processed/reporte_clinica_procesado.csv"

if os.path.exists(ruta_datos):
    df = pd.read_csv(ruta_datos)
    
    st.sidebar.header("Filtros de Visualización")
    opcion_sexo = st.sidebar.multiselect("Filtrar por Sexo:", options=df['sex'].unique(), default=df['sex'].unique())
    
    # Filtrar datos según la barra lateral
    df_filtrado = df[df['sex'].isin(opcion_sexo)]
    
    # Gráfico 1: Edad vs Costos de Facturación
    st.subheader("🎯 Relación entre Edad y Costos Médicos")
    fig1, ax1 = plt.subplots(figsize=(10, 4))
    sns.scatterplot(data=df_filtrado, x='age', y='charges', hue='smoker', palette='Set1', alpha=0.7, ax=ax1)
    ax1.set_title("Cargos de Facturación según la Edad y Hábito de Fumar")
    ax1.set_xlabel("Edad")
    ax1.set_ylabel("Costos ($)")
    st.pyplot(fig1)
    
    # Gráfico 2: Distribución por Región
    st.subheader("🌍 Costos Promedio por Región Geográfica")
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    sns.barplot(data=df_filtrado, x='region', y='charges', hue='sex', palette='muted', errorbar=None, ax=ax2)
    ax2.set_title("Comparativa de Costos por Región y Sexo")
    ax2.set_xlabel("Región")
    ax2.set_ylabel("Costo Promedio ($)")
    st.pyplot(fig2)
    
else:
    st.error("⚠️ No se encontró el archivo 'reporte_clinica_procesado.csv' en 'data/processed/'.")
