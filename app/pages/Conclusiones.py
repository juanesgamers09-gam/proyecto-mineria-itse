import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Conclusiones del Proyecto", page_icon="🎓", layout="wide")
st.title("🎓 Conclusiones y Recomendaciones Estratégicas")
st.markdown("---")

ruta_datos = "data/processed/reporte_clinica_procesado.csv"

if os.path.exists(ruta_datos):
    df = pd.read_csv(ruta_datos)
    
    # Calcular algunas métricas rápidas de soporte para las conclusiones
    costo_fumador = df[df['smoker'] == 'yes']['charges'].mean()
    costo_no_fumador = df[df['smoker'] == 'no']['charges'].mean()
    diferencia_veces = costo_fumador / costo_no_fumador
    
    st.subheader("📌 Hallazgos Clave de la Minería de Datos")
    
    st.markdown(f"""
    1. **Impacto Crítico del Tabaquismo:** A través del análisis exploratorio (EDA) y la distribución de costos, se determinó que los pacientes fumadores tienen un costo médico promedio significativamente mayor en comparación con los no fumadores. En este conjunto de datos, un fumador promedia cargos que representan aproximadamente **{diferencia_veces:.1f} veces** el costo de un no fumador.
    2. **Estructura de Dimensiones:** El proceso ETL aplicado removió registros nulos y duplicados, consolidando un pipeline de datos limpio y listo para auditorías institucionales con un total de `{df.shape[0]}` registros estables.
    3. **Reducción de Dimensionalidad (PCA):** La aplicación de Componentes Principales demostró que variables numéricas como la edad y los cargos explican la mayor parte de la varianza del comportamiento de la facturación de la clínica.
    """)
    
    st.subheader("💡 Recomendaciones del Negocio / Clínicas")
    st.info("""
    * **Programas de Prevención:** Desarrollar políticas de salud internas o planes de incentivos para la reducción del tabaquismo, dado que impacta directamente en las primas y costos de facturación.
    * **Segmentación de Tarifas:** Utilizar los modelos predictivos explorados para ajustar presupuestos financieros anuales basados en los perfiles demográficos de los pacientes ingresados.
    """)
    
else:
    st.error("⚠️ No se encontró el archivo 'reporte_clinica_procesado.csv' en 'data/processed/'.")
