import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Análisis de PCA", page_icon="🧬", layout="wide")
st.title("🧬 Análisis de Componentes Principales (PCA)")
st.markdown("---")

ruta_datos = "data/processed/reporte_clinica_procesado.csv"

if os.path.exists(ruta_datos):
    df = pd.read_csv(ruta_datos)
    
    st.markdown("""
    El análisis de PCA ayuda a reducir la cantidad de variables numéricas correlacionadas, 
    proyectándolas en nuevas dimensiones llamadas **Componentes Principales (PC)**.
    """)
    
    # Seleccionar solo columnas numéricas para PCA
    columnas_numericas = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    
    st.sidebar.header("Configuración de PCA")
    variables_seleccionadas = st.sidebar.multiselect(
        "Selecciona las variables para el PCA:",
        options=columnas_numericas,
        default=columnas_numericas
    )
    
    if len(variables_seleccionadas) >= 2:
        X = df[variables_seleccionadas]
        
        # Estandarizar los datos (Paso obligatorio para PCA)
        X_scaled = StandardScaler().fit_transform(X)
        
        # Aplicar PCA para 2 componentes principales
        pca = PCA(n_components=2)
        componentes = pca.fit_transform(X_scaled)
        
        df_pca = pd.DataFrame(data=componentes, columns=['Componente 1', 'Componente 2'])
        
        # Añadir variable categórica para colorear el gráfico si existe
        if 'smoker' in df.columns:
            df_pca['Fumador'] = df['smoker']
            hue_opcion = 'Fumador'
        else:
            hue_opcion = None
            
        # Gráfico de Varianza Explicada
        st.subheader("📊 Varianza Explicada por cada Componente")
        varianza = pca.explained_variance_ratio_
        st.write(f"**Componente 1:** explica el {varianza[0]*100:.2f}% de la varianza total.")
        st.write(f"**Componente 2:** explica el {varianza[1]*100:.2f}% de la varianza total.")
        
        # Gráfico de Dispersión PCA
        st.subheader("🎯 Proyección de los Pacientes en el Espacio PCA (2D)")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(data=df_pca, x='Componente 1', y='Componente 2', hue=hue_opcion, palette='Set1', alpha=0.8, ax=ax)
        ax.set_title("Gráfico de Dispersión de las dos Primeras Componentes Principales")
        st.pyplot(fig)
        
    else:
        st.warning("⚠️ Debes seleccionar al menos 2 variables numéricas para poder ejecutar el análisis de PCA.")
else:
    st.error("⚠️ No se encontró el archivo 'reporte_clinica_procesado.csv' en 'data/processed/'.")
