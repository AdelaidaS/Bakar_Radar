import streamlit as st
import requests
import shutil

# Nombre del archivo PDF y la miniatura
pdf_filename = "Informe_BakarRadar.pdf"
thumbnail_filename = "miniatura_informe.png"

# Miniatura del informe
st.image(thumbnail_filename, caption="Vista previa del informe")

# Botón para descargar el informe
if st.button("Descargar Informe"):
    # Descargar el archivo PDF
    with open(pdf_filename, "rb") as file:
        data = file.read()
    with open("Informe_BakarRadar.pdf", "wb") as file:
        file.write(data)
    # Mostrar un mensaje de éxito
    st.success("Informe descargado correctamente.")

    # Mover el archivo PDF al directorio actual
    shutil.move(pdf_filename, "Informe_BakarRadar.pdf")
