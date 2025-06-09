import streamlit as st
import funciones

st.title("Dispersion")

if "lineas" not in st.session_state:
    st.session_state.lineas = []

#dato 1
tipo_documento = st.selectbox("Tipo de documento",["CC","TI","CE","RC","PA"])

#dato 2
documento = st.text_input("Numero de documento")

if st.button("Generar"):
    
    linea_completa = funciones.crear_dispersion(tipo_documento,documento)
    
    st.session_state.lineas.append(linea_completa)
    
st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.lineas, 1):
    st.text(f"{linea}")