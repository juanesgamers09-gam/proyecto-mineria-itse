import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Análisis del Dataset", page_icon="📊", layout="wide")
st.title("📊 Análisis Exploratorio de Datos (EDA)")
st.markdown("---")

ruta_datos = "data/processed/reporte_clinica_procesado.csv"

if os.path.exists(ruta_datos):
    df = pd.read_csv(ruta_datos)
    st.subheader("📋 Dimensiones y Estructura")
    st.markdown(f"El dataset limpio cuenta con **{df.shape[0]}** registros y **{df.shape[1]}** variables.")
    
    st.subheader("👀 Vista previa de los registros limpios")
    st.dataframe(df.head(10))
    
    st.subheader("⚙️ Propiedades de las Variables")
    info_df = pd.DataFrame({
        "Tipo de Variable": df.dtypes.astype(str),
        "Valores Válidos": df.notnull().sum(),
        "Valores Faltantes (Nulos)": df.isnull().sum()
    })
    st.dataframe(info_df)
    
    st.subheader("🔢 Resumen Estadístico de Valores Numéricos")
    st.dataframe(df.describe())
    
    st.subheader("📈 Visualización de Distribución de Costos")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.boxplot(data=df, x='smoker', y='charges', palette='Set2', ax=ax)
    st.pyplot(fig)
else:
    st.error("⚠️ No se encontró el archivo de datos en la ruta especificada.")
