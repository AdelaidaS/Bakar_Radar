import streamlit as st
import pandas as pd
import pickle

def classify(num):
    if num == 0:
        return "Riesgo BAJO."
    elif num == 1:
        return "Riesgo MEDIO. Revisar datos individualizados."
    elif num == 2:
        return "Riesgo ALTO de Soledad no deseada. Establecer acciones inmediatas."


def load_model():
    with open('best_model_clasif_multi.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

def classify_result(result):
    # Clasificación basada en el resultado
    return classify(result)

def mapear_edad(edad):
    # Mapeo de edad
    return edad

# Mapeo de variables categóricas
mapeo_estado_civil = {'soltero': 0, 'casado': 1, 'divorciado': 2, 'viudo': 3}
mapeo_sexos = {'hombre': 0, 'mujer': 1}
mapeo_nivel_estudios = {'sin estudios': 0, 'primarios': 1, 'secundarios': 2, 'terciarios': 3, 'universitarios': 4}
mapeo_psicofarmacos = {'no': 0, 'sí': 1}
mapeo_vive_solo = {'no': 0, 'sí': 1}
mapeo_hijos = {'no': 0, 'sí': 1}
mapeo_ascensor = {'no': 0, 'sí': 1}
mapeo_act_fisica = {'sedentario': 0, 'ligera': 1, 'moderada': 2, 'intensa': 3}
mapeo_lim_fisica = {'sin limitaciones': 0, 'limitaciones leves': 1, 'limitaciones moderadas': 2, 'limitaciones graves': 3}
mapeo_estado_animo = {'bajo': 0, 'medio': 1, 'alto': 2}
mapeo_satisfaccion_vida = {'baja': 0, 'media': 1, 'alta': 2}
mapeo_ingresos_economicos = {'bajos': 0, 'medios': 1, 'altos': 2}
mapeo_red_apoyo_familiar = {'baja': 0, 'media': 1, 'alta': 2}
mapeo_cohesion_social = {'baja': 0, 'media': 1, 'alta': 2}
mapeo_municipio_accesible = {'no': 0, 'sí': 1}
mapeo_municipio_rec_social = {'no': 0, 'sí': 1}
mapeo_municipio_rec_ocio = {'no': 0, 'sí': 1}

def user_input_parameters():
    st.sidebar.subheader("Parámetros de entrada")
    edad = st.sidebar.number_input("Edad", min_value=0, max_value=100, value=50)
    estado_civil = st.sidebar.selectbox("Estado civil", list(mapeo_estado_civil.keys()))
    sexo = st.sidebar.selectbox("Sexo", list(mapeo_sexos.keys()))
    nivel_estudios = st.sidebar.selectbox("Nivel de estudios", list(mapeo_nivel_estudios.keys()))
    psicofarmacos = st.sidebar.selectbox("¿Consume psicofármacos?", list(mapeo_psicofarmacos.keys()))
    vive_solo = st.sidebar.selectbox("¿Vive solo/a?", list(mapeo_vive_solo.keys()))
    hijos = st.sidebar.selectbox("¿Tiene hijos?", list(mapeo_hijos.keys()))
    ascensor = st.sidebar.selectbox("¿Tiene ascensor en el edificio?", list(mapeo_ascensor.keys()))
    act_fisica = st.sidebar.selectbox("Actividad física", list(mapeo_act_fisica.keys()))
    lim_fisica = st.sidebar.selectbox("Limitaciones físicas", list(mapeo_lim_fisica.keys()))
    estado_animo = st.sidebar.selectbox("Estado de ánimo", list(mapeo_estado_animo.keys()))
    satisfaccion_vida = st.sidebar.selectbox("Satisfacción con la vida", list(mapeo_satisfaccion_vida.keys()))
    ingresos_economicos = st.sidebar.selectbox("Ingresos económicos", list(mapeo_ingresos_economicos.keys()))
    red_apoyo_familiar = st.sidebar.selectbox("Red de apoyo familiar", list(mapeo_red_apoyo_familiar.keys()))
    cohesion_social = st.sidebar.selectbox("Cohesión social", list(mapeo_cohesion_social.keys()))
    municipio_accesible = st.sidebar.selectbox("¿Municipio accesible?", list(mapeo_municipio_accesible.keys()))
    municipio_rec_social = st.sidebar.selectbox("¿Municipio con recursos sociales?", list(mapeo_municipio_rec_social.keys()))
    municipio_rec_ocio = st.sidebar.selectbox("¿Municipio con recursos de ocio?", list(mapeo_municipio_rec_ocio.keys()))

    estado_civil_num = mapeo_estado_civil.get(estado_civil)
    sexo_num = mapeo_sexos.get(sexo)
    nivel_estudios_num = mapeo_nivel_estudios.get(nivel_estudios)
    psicofarmacos_num = mapeo_psicofarmacos.get(psicofarmacos)
    vive_solo_num = mapeo_vive_solo.get(vive_solo)
    hijos_num = mapeo_hijos.get(hijos)
    ascensor_num = mapeo_ascensor.get(ascensor)
    act_fisica_num = mapeo_act_fisica.get(act_fisica)
    lim_fisica_num = mapeo_lim_fisica.get(lim_fisica)
    estado_animo_num = mapeo_estado_animo.get(estado_animo)
    satisfaccion_vida_num = mapeo_satisfaccion_vida.get(satisfaccion_vida)
    ingresos_economicos_num = mapeo_ingresos_economicos.get(ingresos_economicos)
    red_apoyo_familiar_num = mapeo_red_apoyo_familiar.get(red_apoyo_familiar)
    cohesion_social_num = mapeo_cohesion_social.get(cohesion_social)
    municipio_accesible_num = mapeo_municipio_accesible.get(municipio_accesible)
    municipio_rec_social_num = mapeo_municipio_rec_social.get(municipio_rec_social)
    municipio_rec_ocio_num = mapeo_municipio_rec_ocio.get(municipio_rec_ocio)

    user_parameters = {
        'edad': mapear_edad(edad),
        'estado_civil': estado_civil_num,
        'sexo': sexo_num,
        'nivel_estudios': nivel_estudios_num,
        'psicofarmacos': psicofarmacos_num,
        'vive_solo': vive_solo_num,
        'hijos': hijos_num,
        'ascensor': ascensor_num,
        'act_fisica': act_fisica_num,
        'lim_fisica': lim_fisica_num,
        'estado_animo': estado_animo_num,
        'satisfaccion_vida': satisfaccion_vida_num,
        'ingresos_economicos': ingresos_economicos_num,
        'red_apoyo_familiar': red_apoyo_familiar_num,
        'cohesion_social': cohesion_social_num,
        'municipio_accesible': municipio_accesible_num,
        'municipio_rec_social': municipio_rec_social_num,
        'municipio_rec_ocio': municipio_rec_ocio_num
    }

    return user_parameters

def run_model(user_selections, model):
    result = model.predict(user_selections)[0]
    classification = classify_result(result)
    return classification


model = load_model()

user_parameters = user_input_parameters()

with st.container(): st.write("Parametros seleccionados por el usuario:")
user_selections = pd.DataFrame([user_parameters])
st.write(user_selections)

if st.button("Run"):
    result = run_model(user_selections, model)
    st.write(result)
