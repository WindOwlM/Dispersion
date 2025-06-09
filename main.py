import streamlit as st
import funciones
import datetime

st.title("Dispersion")

if "lineas" not in st.session_state:
    st.session_state.lineas = []

#INICIO FORM
min_value = datetime.date(2000,1,1)

#dato 1
tipo_documento = st.selectbox("Tipo de documento",["CC","TI","CE","RC","PA"])

#dato 2
documento = st.text_input("Numero de documento")

#dato 3
primer_apellido = st.text_input("Primer apellido")

#dato 4
segundo_apellido = st.text_input("Segundo apellido")
    
#dato 5
primer_nombre = st.text_input("Primer nombre")
    
#dato 6
segundo_nombre = st.text_input("Segundo nombre")

#dato 7
periodo_nomina = st.date_input("Periodo Nomina", min_value=min_value)

periodo_nomina_anio = periodo_nomina.year
periodo_nomina_mes = periodo_nomina.month

#dato 8
referencia = st.text_input("Referencia emitida por colpensiones")

#dato 9
banco = st.text_input("Codigo de banco (2 digitos max)", max_chars=2)

#dato 10
sucursal = st.text_input("Codigo de la sucursal del banco (4 digitos max)", max_chars=4)

#dato 11
cuenta = st.text_input("Cuenta (Debe ser 0 si es ventanilla)")

#dato 12
tipo_cuenta = st.selectbox("Tipo de cuenta",["CA","CP","CC","VE"])

#dato 13
valor_neto = st.text_input("Valor neto")

#dato 14
tipo_documento_ant = st.selectbox("Tipo de documento anterior",["CC","TI","CE","RC","PA"])

#dato 15
documento_ant = st.text_input("Numero de documento anterior")

#dato 16
fecha_gen_mageti = st.date_input("Fecha Generación del Magnético", min_value=min_value)

#dato 17
fecha_apli_pag = st.date_input("Fecha Aplicación Pago", min_value=min_value)

#dato 18
tipo_documento_repre = st.selectbox("Tipo de documento del representante legal",["CC","TI","CE","RC","PA"])

#dato 19
documento_repre = st.text_input("Numero de documento del representante legal")

#dato 20
primer_apellido_repre = st.text_input("Primer apellido del representante legal")

#dato 21
segundo_apellido_repre = st.text_input("Segundo apellido del representante legal")
    
#dato 22
primer_nombre_repre = st.text_input("Primer nombre del representante legal")
    
#dato 23
segundo_nombre_repre = st.text_input("Segundo nombre del representante legal")

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
                                                sucursal,
                                                cuenta,
                                                tipo_cuenta,
                                                valor_neto,
                                                tipo_documento_ant,
                                                documento_ant,
                                                fecha_gen_mageti,
                                                fecha_apli_pag,
                                                tipo_documento_repre,
                                                documento_repre,
                                                primer_apellido_repre,
                                                segundo_apellido_repre,
                                                primer_nombre_repre,
                                                segundo_nombre_repre)
    
    st.session_state.lineas.append(linea_completa)
    
st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.lineas, 1):
    st.text(f"{linea}")