import streamlit as st
import funciones
import datetime

st.title("Dispersion")
min_value = datetime.date(2000,1,1)

if "lineas" not in st.session_state:
    st.session_state.lineas = []
    st.session_state.cupones = []
    st.session_state.onp = []

with st.expander("Linea 1"):

    #INICIO FORM

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

    if st.button("Generar linea 1"):
        
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

with st.expander("Linea 2"):
    
    #dato 1
    fecha_hora = st.text_input("Fecha y Hora de pago del archivo (AAAAMMDDHHMMSS)", max_chars=14)

    #dato 2
    cantidad_total_registros=st.text_input("Cantitad total de registros de mesadas a procesar", max_chars=8)

    #dato 3
    valor_total_pagos=st.text_input("Valor total de los pagos", max_chars=18)

    #dato 4
    cantidad_registros_abono_cuenta=st.text_input("Cantitad de registros por abono en cuenta", max_chars=8)

    #dato 5
    valor_total_abono=st.text_input("Valor total abono en cuenta", max_chars=18)

    #dato 6
    cantidad_registros_pago_ventanilla=st.text_input("Cantitad de registros pago por ventanilla", max_chars=8)

    #dato 7 
    valor_total_pago_ventanilla=st.text_input("Valor total pago por ventanillas", max_chars=18)

    #dato 8
    tipo_cuenta_dispersora = st.selectbox("Tipo de cuenta dispersadora originadora 1 - CTA.Corriente, 2 - Cuenta ahorros",["1","2"])

    #dato 9
    numero_cuenta_dispersora=st.text_input("Numero de la cuenta dispersora", max_chars=15)

    #dato 10
    tipo_identificacion_empresa_dispersora = st.selectbox("Tipo de identificacion de la empresa dispersora (Siempre debe ser N - NIT)",["N"])

    #dato 11
    num_identificacion_empresa =st.text_input("Numero de identifiacion de la empresa originadora", max_chars=12)

    if st.button("Generar linea 2"):
        
        linea_completa = funciones.crear_linea_2(fecha_hora,
                                                 cantidad_total_registros,
                                                 valor_total_pagos,
                                                 cantidad_registros_abono_cuenta,
                                                 valor_total_abono,
                                                 cantidad_registros_pago_ventanilla,
                                                 valor_total_pago_ventanilla,
                                                 tipo_cuenta_dispersora,
                                                 numero_cuenta_dispersora,
                                                 tipo_identificacion_empresa_dispersora,
                                                 num_identificacion_empresa)
        st.session_state.lineas.append(linea_completa)

st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.lineas, 1):
    st.text(f"{linea}")
    
    
st.title("Cupones")

with st.expander("Linea 1"):
    
    #dato 1
    cod_ent_bancaria = st.text_input("Codigo de entidad bancaria",max_chars=3)
    
    #dato 2
    nom_ent_banco = st.text_input("Nombre de la entidad bancaria",max_chars=50)
    
    #dato 3
    cant_sucursal = st.text_input("Cantidad de sucursales por entidad bancaria",max_chars=4)
    
    #dato 4
    cant_pensionados = st.text_input("Cantidad de pensionados por entidad bancaria",max_chars=7)
    
    #dato 5
    anio_nomina = st.text_input("Año nomina (AAAA)",max_chars=4)
    
    #dato 6
    mes_nomina = st.text_input("Mes nomina (MM)",max_chars=2)
    
    #dato 7
    fech_vence = st.text_input("Fecha de vencimiento (DD/MM/AAAA)",max_chars=10)
    
    #dato 8
    mensaje = st.text_area("Mensaje variable",max_chars=250)
    
    if st.button("Generar linea cupones 1"):
        
        linea_completa = funciones.cupones_1(cod_ent_bancaria,
                                             nom_ent_banco,
                                             cant_sucursal,
                                             cant_pensionados,
                                             anio_nomina,
                                             mes_nomina,
                                             fech_vence,
                                             mensaje)
        
        st.session_state.cupones.append(linea_completa)

with st.expander("Linea 2"):
    
    #dato 1
    num_cupon = st.text_input("Numero de cupon",max_chars=12)
    
    #dato 2
    tipo_documento_cupon_1 = st.selectbox("Tipo de documento cupon 1",["CC","TI","CE"])
    
    #dato 3
    num_documento_cupon_1 = st.text_input("Numero documento pensionado", max_chars=15)
    
    #dato 4
    primer_apellido_cupon = st.text_input("Primer apellido cupones", max_chars=15)

    #dato 5
    segundo_apellido_cupon = st.text_input("Segundo apellido cupones", max_chars=15)
        
    #dato 6
    primer_nombre_cupon = st.text_input("Primer nombre cupones", max_chars=15)
        
    #dato 7
    segundo_nombre_cupon = st.text_input("Segundo nombre cupones", max_chars=15)

    #dato 8
    cod_sucursal_entidad = st.text_input("Codigo sucursal entidad bancaria",max_chars=4)
    
    #dato 9
    nom_suc_ent_bancaria = st.text_input("Codigo sucursal entidad bancaria",max_chars=25)
    
    #dato 10
    num_cuenta_cupon = st.text_input("Numero de cuenta",max_chars=17)
    
    #dato 11
    direc_sucursal = st.text_input("Dirección Sucursal Entidad Bancaria",max_chars=45)
    
    #dato 12
    cod_depart_dane = st.text_input("Código Departamento-Dane Sucursal Entidad Bancaria",max_chars=2)
    
    #dato 13
    nom_depart_sucursal = st.text_area("Nombre Departamento Sucursal Entidad Bancaria",max_chars=50)
    
    #dato 14
    cod_ciudad_dane = st.text_input("Código Ciudad/Municipio-Dane Sucursal Entidad Bancaria",max_chars=3)
    
    #dato 15
    nom_ciudad_sucursal = st.text_area("Nombre Ciudad/Municipio Sucursal Entidad Bancaria",max_chars=50)
    
    if st.button("Generar linea cupones 2"):
        
        linea_completa = funciones.cupones_2(num_cupon,
                                            tipo_documento_cupon_1,
                                            num_documento_cupon_1,
                                            primer_apellido_cupon,
                                            segundo_apellido_cupon,
                                            primer_nombre_cupon,
                                            segundo_nombre_cupon,
                                            cod_sucursal_entidad,
                                            nom_suc_ent_bancaria,
                                            num_cuenta_cupon,
                                            direc_sucursal,
                                            cod_depart_dane,
                                            nom_depart_sucursal,
                                            cod_ciudad_dane,
                                            nom_ciudad_sucursal)
        
        st.session_state.cupones.append(linea_completa)
        
with st.expander("linea 3"):
    
    #dato 1
    tipo_documento_cupon_2 = st.selectbox("Tipo de documento cupon 2",["CC","TI","CE"])

st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.cupones, 1):
    st.text(f"{linea}")


#De aqui para abajo es Ordenes de no pago
st.title("Ordenes de no pago")

with st.expander("Linea 1"):
    
    #dato 1
    tipo_documento = st.selectbox("Tipo de documento",["CC","CE","RC","TI","PA"])



    
    if st.button("Generar linea onp 1"):
        
        linea_completa = funciones.Orden_no_pago(tipo_documento)
        
        st.session_state.onp.append(linea_completa)

st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.onp, 1):
    st.text(f"{linea}")
