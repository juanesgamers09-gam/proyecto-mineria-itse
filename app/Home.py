import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de la página
st.set_page_config(page_title="Dashboard Clínico", layout="wide")

st.title("🏥 Análisis de Costos Clínicos y Facturación Médica")
st.write("Bienvenido al sistema interactivo de minería de datos.")

# Rutas a los datos procesados
ruta_datos = "data/processed/reporte_clinica_procesado.csv"

if os.path.exists(ruta_datos):
    df = pd.read_csv(ruta_datos)
    
    # Métricas principales
    st.subheader("📊 Resumen General")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Pacientes", f"{len(df):,}")
    col2.metric("Costo Promedio ($)", f"{df['charges'].mean():,.2f}")
    col3.metric("Edad Promedio", f"{df['age'].mean():.1f} años")
    
    # Gráfico interactivo
    st.subheader("📈 Distribución de Costos por Fumador / No Fumador")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=df, x='smoker', y='charges', palette='Set2', ax=ax)
    ax.set_title("Costos Médicos en relación al hábito de fumar")
    st.pyplot(fig)
    
    # Mostrar tabla de datos
    st.subheader("📋 Vista previa de los datos limpios")
    st.dataframe(df.head(10))
else:
    st.warning("⚠️ No se encontró el archivo de datos en `data/processed/reporte_clinica_procesado.csv`. Asegúrate de subirlo a GitHub.")
