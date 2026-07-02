# 🏥 Proyecto Semestral: Análisis de Costos Clínicos y Facturación Médica

Este repositorio contiene el desarrollo completo del proyecto de la materia **Minería de Datos 1**. El objetivo principal es la implementación de un flujo integral (Pipeline) que abarca la extracción de datos de facturación médica, su limpieza y transformación (ETL), el análisis exploratorio (EDA) y su posterior visualización en una plataforma interactiva pública.

---

## 👥 Información General del Autor
* **Estudiante:** Montero Juan
* **Institución:** Instituto Técnico Superior Especializado (ITSE)
* **Facultad:** Escuela de Tecnología de la Información y Comunicación
* **Materia:** Minería de Datos 1
* **Año Académico:** 2026

---

## 📂 Estructura Organizada del Proyecto

Cumpliendo estrictamente con los estándares exigidos para la gestión de proyectos de ciencia de datos, la estructura del repositorio se distribuye de la siguiente manera:

* **`data/`**: Gestión de los conjuntos de datos del proyecto.
  * `raw/`: Contiene el archivo original sin modificaciones (`reporte_clinica (3).csv`).
  * `processed/`: Almacena el dataset limpio tras remover nulos y duplicados (`reporte_clinica_procesado.csv`).
* **`notebooks/`**: Cuadernos interactivos de Google Colab donde se desarrolla paso a paso el código de limpieza y análisis exploratorio.
* **`app/`**: Contiene la solución de software interactiva desplegada en producción.
  * `Home.py`: Página de inicio de la aplicación Streamlit.
  * `pages/`: Subcarpeta que contiene los módulos complementarios como `Dataset.py`.
* **`reports/`**: Espacio asignado para almacenar el informe técnico ejecutivo final del análisis en formato PDF.
* **`logs/`**: Registros de auditoría del sistema. Contiene el archivo `pipeline_log.csv` que detalla las métricas de la transformación ETL de forma estructurada.
* **`requirements.txt`**: Archivo de configuración en la raíz del repositorio que enumera las librerías necesarias de Python.

---

## 🚀 Guía de Instalación y Ejecución

### 1. Clonar el repositorio e instalar dependencias
Para reproducir este entorno de forma local o en servidores cloud, ejecute los siguientes comandos en su terminal:

```bash
# Clonar este repositorio
git clone [https://github.com/juanesgamers09-gam/proyecto-mineria-itse.git](https://github.com/juanesgamers09-gam/proyecto-mineria-itse.git)

# Acceder al directorio
cd proyecto-mineria-itse

# Instalar los requerimientos necesarios
pip install -r requirements.txt
