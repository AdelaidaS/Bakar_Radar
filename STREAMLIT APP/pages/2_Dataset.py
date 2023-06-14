import streamlit as st
import pandas as pd
from PIL import Image
import os

# Título
st.subheader("Datos empleados para el modelo de Machine Learning.")
st.write("A través de un estudio exhaustivo del Estado del Arte en individuos mayores de 65 años de edad, hemos desarrollado un modelo de Machine Learning en el que, analizando variables relacionadas con el individuo, entorno social y datos demográficos, se puede predecir el nivel de soledad no deseada que sufre un individuo, colectivo o incluso población.")
st.write("La base de datos que hemos generado consta de 17 variables de atributos como edad, sexo, estado civil, ingresos económicos, recursos sociales y de ocio del municipio, sentimiento de bienestar, etc.")
st.write("Se han empleado 5001 registros que se han modelado frente al target: nivel de soledad, de forma que se obtienen 3 niveles:")
st.write("  Nivel soledad 0 = riesgo bajo de soledad no deseada")
st.write("  Nivel soledad 1 = riesgo medio de soledad no deseada")
st.write("  Nivel soledad 2 = riesgo alto de soledad no deseada")

# Carga del dataset
df = pd.read_csv("./pages/df_soledad_DEF.csv")

# Título
st.subheader("Información del Dataset:")

# Explicación del contenido del dataset
column1, column2, column3 = st.columns(3)

column1.write("Edad")
column1.write("Estado civil")
column1.write("Género")
column1.write("Nivel de estudios")
column1.write("Psicofármacos")
column1.write("Vivir solo")

column2.write("Hijos")
column2.write("Ascensor")
column2.write("Actividad física")
column2.write("Limitaciones físicas")
column2.write("Estado de ánimo")
column2.write("Satisfacción con la vida")

column3.write("Ingresos económicos")
column3.write("Red de apoyo familiar")
column3.write("Cohesión social")
column3.write("Municipio accesible")
column3.write("Recursos sociales del municipio")
column3.write("Recursos de ocio del municipio")

# Botón de descarga del dataset
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

# Botón de descarga
st.download_button(
    label="Descargar el dataset",
    data=csv,
    file_name="file.csv",
    mime="text/csv",
    key='download-csv'
)

# Visualización del dataset con las columnas en la orientación vertical
df_transposed = df.transpose()
st.dataframe(df_transposed)

# Obtener la ruta relativa de la imagen
image_path = os.path.join(os.path.dirname(__file__), "correlacion_modelo.png")
image = Image.open(image_path)
st.image(image, use_column_width=True)
