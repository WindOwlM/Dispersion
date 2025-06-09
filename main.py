import streamlit as st
import funciones

st.title("Dispersion")

if "lineas" not in st.session_state:
    st.session_state.lineas = []

#INICIO FORM

#dato 1
tipo_documento = st.selectbox("Tipo de documento",["CC","TI","CE","RC","PA"])

#dato 2
documento = st.text_input("Numero de documento")

#dato 4
primer_apellido = st.text_input("Primer apellido")

#dato 5
segundo_apellido = st.text_input("Segundo apellido")
    
#dato 6
primer_nombre = st.text_input("Primer nombre")
    
#dato 7
segundo_nombre = st.text_input("Segundo nombre")

#dato 8
periodo_nomina = st.date_input("Periodo Nomina")

periodo_nomina_anio = periodo_nomina.year
periodo_nomina_mes = periodo_nomina.month

#dato 9
referencia = st.text_input("Referencia emitida por colpensiones")

#dato 10
banco = st.text_input("Codigo de banco")

#dato 11
sucursal = st.text_input("Codigo de la sucursal del banco")

#FIN FORM    

if st.button("Generar"):
    
    linea_completa = funciones.crear_dispersion(tipo_documento,
                                                documento,
                                                primer_apellido,
                                                segundo_apellido,
                                                primer_nombre,
                                                segundo_nombre,
                                                periodo_nomina_anio,
                                                periodo_nomina_mes,
                                                referencia,
                                                banco,
                                                sucursal)
    
    st.session_state.lineas.append(linea_completa)
    
st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.lineas, 1):
    st.text(f"{linea}")