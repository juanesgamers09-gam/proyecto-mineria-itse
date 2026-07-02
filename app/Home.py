import streamlit as st
import pandas as pd
import os

# Configuración formal de la página interactiva
st.set_page_config(
    page_title="Dashboard de Costos Clínicos",
    page_icon="🏥",
    layout="wide"
)

# Título Principal e Introducción Institucional
st.title("🏥 Solución Analítica: Costos Clínicos y Facturación Médica")
st.markdown("---")

st.markdown("""
## 📊 Bienvenida al Sistema Interactiva de Minería de Datos

Esta plataforma web ha sido desarrollada como parte del **Proyecto Semestral de Minería de Datos 1** en el **Instituto Técnico Superior Especializado (ITSE)**. 

El propósito de esta aplicación es proveer una interfaz visual y dinámica para auditar, explorar y comprender las variables que impactan directamente en la facturación y los costos médicos de la institución clínica.

### 🔍 ¿Qué encontrará en este Dashboard?
* **Página Principal (Home):** Vista de bienvenida, objetivos institucionales e indicadores clave globales del negocio.
* **Análisis Exploratorio (Dataset):** Acceso estructurado a las dimensiones de la base de datos, tipos de variables y el comportamiento estadístico de los registros limpios.
""")

st.sidebar.success("Seleccione una pestaña arriba para navegar.")

# Intentar cargar métricas rápidas globales en el inicio si el archivo procesado existe
ruta_datos = "data/processed/reporte_clinica_procesado.csv"

if os.path.exists(ruta_datos):
    df = pd.read_csv(ruta_datos)
    
    st.subheader("📈 Indicadores Clave de Rendimiento (KPIs Globales)")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total Registros Auditados", value=f"{df.shape[0]:,}")
    with col2:
        st.metric(label="Costo Médico Promedio", value=f"${df['charges'].mean():,.2f}")
    with col3:
        st.metric(label="Edad Promedio de Pacientes", value=f"{df['age'].mean():.1f} años")
else:
    st.info("💡 Nota: Los KPIs globales se activarán automáticamente una vez que el archivo procesado esté disponible en el servidor de producción.")
