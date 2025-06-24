import streamlit as st
import funciones
import datetime

st.title("Dispersion")
min_value = datetime.date(2000,1,1)

if "lineas" not in st.session_state:
    st.session_state.lineas = []
    st.session_state.cupones = []
    st.session_state.onp = []
    st.session_state.preapertura = []

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

    #dato 8 aqui inician los campos de referencia
    ref_tipo_documento = st.selectbox("Tipo de documento referencia",["CC","TI","CE","RC","PA"])

    #dato 2 de referencia
    ref_num_doc = st.text_input("Numero documento referencia", max_chars=12)

    #dato 3 de referencia
    ref_fech = st.date_input("Fecha referencia(AAAAMMDD)",  min_value=min_value)

    #dato 4 de referencia
    ref_id_pension = st.text_input("Id de la pension referencia", max_chars=8)

    #dato 5 de referencia
    ref_espacios_blanco = st.text_input("12 espacios en blanco", disabled=True)

    #dato 6 de referencia
    ref_fech2 = st.date_input("Fecha referencia 2(AAAAMMDD)",  min_value=min_value)

    #dato 9
    banco = st.text_input("Codigo de banco (2 digitos max)", max_chars=2)

    #dato 10
    sucursal = st.text_input("Codigo de la sucursal del banco (4 digitos max)", max_chars=4)

    #dato 11
    cuenta = st.text_input("Cuenta (Debe ser 0 si es ventanilla)", max_chars=20)

    #dato 12
    tipo_cuenta = st.selectbox("Tipo de cuenta",["CA","CP","CC","VE"])

    #dato 13
    valor_neto = st.text_input("Valor neto")

    #dato 14
    tipo_documento_ant = st.text_input("Tipo de documento anterior",disabled=True)

    #dato 15
    documento_ant = st.text_input("Numero de documento anterior", disabled=True) 

    #dato 16
    fecha_gen_mageti = st.date_input("Fecha Generación del Magnético", min_value=min_value)

    #dato 17
    fecha_apli_pag = st.date_input("Fecha Aplicación Pago", min_value=min_value)

    #dato 18
    tipo_documento_repre = st.text_input("Tipo de documento del representante legal",disabled=True)

    #dato 19
    documento_repre = st.text_input("Numero de documento del representante legal", disabled=True)

    #dato 20
    primer_apellido_repre = st.text_input("Primer apellido del representante legal", disabled=True)

    #dato 21
    segundo_apellido_repre = st.text_input("Segundo apellido del representante legal", disabled=True)
        
    #dato 22
    primer_nombre_repre = st.text_input("Primer nombre del representante legal", disabled=True)
        
    #dato 23
    segundo_nombre_repre = st.text_input("Segundo nombre del representante legal", disabled=True)
    
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
                                                    ref_tipo_documento,
                                                    ref_num_doc,
                                                    ref_fech,
                                                    ref_id_pension,
                                                    ref_espacios_blanco,
                                                    ref_fech2,
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
    
    #dato 2
    num_documento_cupon_2 = st.text_input("Numero de documento cupon 2", max_chars=15)
    
    #dato 3
    tipo_movimiento = st.selectbox("Tipo de movimiento (1 = Devengo 2 = Deducido)",["1","2"])
    
    #dato 4
    con_concept = st.text_input("Codigo concepto", max_chars=5)
    
    #dato 5
    nom_concept = st.text_input("Nombre concepto", max_chars=40)
    
    #dato 6
    var_concept = st.text_input("Valor concepto", max_chars=14)

    if st.button("Generar linea cupones 3"):
        
        linea_completa = funciones.cupones_3(tipo_documento_cupon_2,
                                             num_documento_cupon_2,
                                             tipo_movimiento,
                                             con_concept,
                                             nom_concept,
                                             var_concept)
        
        st.session_state.cupones.append(linea_completa)

with st.expander("linea 4"):
    
    #dato 1
    tipo_documento_cupon_3 = st.selectbox("Tipo de documento cupon 3",["CC","CE"])
    
    #dato 2
    num_documento_cupon_3 = st.text_input("Numero de documento cupon 3", max_chars=15)
    
    #dato 3
    var_devenga = st.text_input("Valor devengados", max_chars=14)
    
    #dato 4
    var_deducidos = st.text_input("Valor deducidos", max_chars=14)
    
    #dato 5
    var_neto = st.text_input("Valor neto", max_chars=14)
    
    #dato 6
    mensaje_per = st.text_area("Valor neto", max_chars=250)
    
    if st.button("Generar linea cupones 4"):
        
        linea_completa = funciones.cupones_4(tipo_documento_cupon_3,
                                             num_documento_cupon_3,
                                             var_devenga,
                                             var_deducidos,
                                             var_neto,
                                             mensaje_per)
        
        st.session_state.cupones.append(linea_completa)

st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.cupones, 1):
    st.text(f"{linea}")


#De aqui para abajo es Ordenes de no pago
st.title("Ordenes de no pago")

with st.expander("Linea 1"):
    
    #dato 1
    tipo_documento = st.selectbox("Tipo de documento",["CC","CE","RC","TI","PA"])

    #dato 2
    num_documento_onp= st.text_input("Numero documento", max_chars=15)
    #dato 3
    primer_apellido_onp= st.text_input("Primer apellido", max_chars=15)

    #dato 4 
    segundo_apellido_onp= st.text_input("Segundo apellido", max_chars=15)

    #dato 5
    primer_nombre_onp= st.text_input("Primer nombre", max_chars=15)

    #dato 6
    segundo_nombre_onp= st.text_input("Segundo nombre", max_chars=15)

    #dato 7
    periodo_nomina_onp= st.text_input("Periodo nomina en formato AAAAMM", max_chars=6)

    #dato 8
    referencia_onp= st.text_input("Referencia (Informacion remitida por Colpensiones)", max_chars=50)
 
    #dato 9
    codigo_banco= st.text_input("Codigo del banco", max_chars=2)

    #dato 10
    sucursal_banco= st.text_input("Codigo de la sucursula del banco",max_chars=4)

    #dato 11
    cuenta_onp= st.text_input("Cuenta (Debe se 0 si el tipo de cuenta es ventanilla)",max_chars=20)

    #dato 12
    tipo_cuenta_onp = st.selectbox("Tipo de cuenta,CA:Cuenta de Ahorros, CP:Cuenta Pensión, CC:Cuenta Corriente, VE:Ventanilla",["CA","CP","CC","VE"])

    #dato 13
    Valor_neto_onp= st.text_input("Valor neto",max_chars=12)

    #dato 14
    estado_pago= st.text_input("Estado pago",max_chars=1)
    
    #dato 15
    fecha_onp = st.text_input("Fecha en la que se remite la ONP por parte de la entidad (AAAAMMDD)", max_chars=8)

    #dato 16
    fecha_fallecimiento = st.text_input("Fecha en la que fallece el beneficiario del pago(AAAAMMDD)", max_chars=8)

    #dato 17
    descripcion_causal_np = st.text_input("Descripcion Causal No pago", max_chars=150)

    #dato 18    
    respuesta_banco = st.text_input("Respuesta banco 0= Reintegrado Total, 1= Pagado, 2= Reintegro Parcial", max_chars=1)

    #dato 19
    valor_reintegro = st.text_input("Valor que la entidad reintegra", max_chars=12)

    #dato 20
    desc_causal_np_banco = st.text_input("Descripcion causal No pago del Banco", max_chars=150)

    #dato 21
    causal_np_banco = st.text_input("Causal No pago del Banco", max_chars=4)

    #dato 22
    fecha_pago_reintegro = st.text_input("Fecha de pago o reintegro Banco(AAAAMMDD)", max_chars=8)

    #dato 23
    hora_pago = st.text_input("Hora en que el banco efectua el pago (HHMMSS)", max_chars=5)



    if st.button("Generar linea onp 1"):
        
        linea_completa = funciones.Orden_no_pago(tipo_documento,
                                                 num_documento_onp,
                                                 primer_apellido_onp,
                                                 segundo_apellido_onp,
                                                 primer_nombre_onp,
                                                 segundo_nombre_onp,
                                                 periodo_nomina_onp,
                                                 referencia_onp,
                                                 codigo_banco,
                                                 sucursal_banco,
                                                 cuenta_onp,
                                                 tipo_cuenta_onp,
                                                 Valor_neto_onp,
                                                 estado_pago,
                                                 fecha_onp,
                                                 fecha_fallecimiento,
                                                 descripcion_causal_np,
                                                 respuesta_banco,
                                                 valor_reintegro,
                                                 desc_causal_np_banco,
                                                 causal_np_banco,
                                                 fecha_pago_reintegro,
                                                 hora_pago)
        
        st.session_state.onp.append(linea_completa)

st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.onp, 1):
    st.text(f"{linea}")


with st.expander("Linea 2"):
    
    #dato 1
    nit_entidad_originadora = st.text_input("Nit entidad originadora", max_chars=12)

    #dato 2
    num_registros_total = st.text_input("Numero de registros total", max_chars=8)

    #dato 3
    valor_total = st.text_input("Valor total", max_chars=18)

    #dato 4
    fecha_generacion = st.text_input("Fecha de generacion (AAAAMMDD)", max_chars=8)

    #dato 5
    hora_generacion = st.text_input("Hora de generacion (HHMMSS)", max_chars=6)




    if st.button("Generar linea onp 2"):
        
        linea_completa = funciones.Orden_no_pago2(nit_entidad_originadora,
                                                  num_registros_total,
                                                  valor_total,
                                                  fecha_generacion,
                                                  hora_generacion)
        
        st.session_state.onp.append(linea_completa)

st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.onp, 1):
    st.text(f"{linea}")

#De aqui para abajo es Preapertura
st.title("Preapertura")

with st.expander("Linea 1"):
    
    #dato 1
    tipo_documento_preapertura = st.selectbox("Tipo de documento preapertura",["CC","CE","RC","TI","PA"])

    #dato 2
    num_documento_prepaertura = st.text_input("Numero de documento", max_chars=15)

    #dato 5 (Sale asi en la tabla compartida por julian)
    primer_apellido_prepaertura = st.text_input("Primer apellido del pensionado", max_chars=15)

    #dato 6 (Sale asi en la tabla compartida por julian)
    segundo_apellido_prepaertura = st.text_input("Segundo apellido del pensionado", max_chars=15)

    #dato 7 (Sale asi en la tabla compartida por julian)
    primer_nombre_prepaertura = st.text_input("Primer nombre del pensionado", max_chars=15)

    #dato 8 (Sale asi en la tabla compartida por julian)
    segunda_nombre_prepaertura = st.text_input("Segundo nombre del pensionado", max_chars=15)

    #dato 9 (Sale asi en la tabla compartida por julian)
    Genero = st.selectbox("Genero: Masculino (M), Femenino (F)",["M","F"])

    #dato 10 (Sale asi en la tabla compartida por julian)
    fecha_nacimiento = st.text_input("Fecha nacimiento (AAAAMMDD)", max_chars=8)
    
    #dato 11 (Sale asi en la tabla compartida por julian)
    direccion_pensionado = st.text_input("Dirreccion de residencia del pensionado", max_chars=45)

    #dato 12 (Sale asi en la tabla compartida por julian)
    telefono_pensionado = st.text_input("Numero de telefono del pensionado", max_chars=7)

    #dato 13 (Sale asi en la tabla compartida por julian)
    celular_pensionado = st.text_input("Numero de celular del pensionado", max_chars=10)

    #dato 14 (Sale asi en la tabla compartida por julian)
    codigo_dep_dane = st.text_input("Código Departamento-Dane", max_chars=2)

    #dato 15 (Sale asi en la tabla compartida por julian)
    nombre_dep = st.text_input("Nombre Departamento", max_chars=50)

    #dato 16 (Sale asi en la tabla compartida por julian)
    cod_ciudad_municipio_dane = st.text_input("Código Ciudad/Municipio-Dane", max_chars=3)
    
    #dato 17 (Sale asi en la tabla compartida por julian)
    nom_ciudad_municipio_dane = st.text_input("Nombre Ciudad/Municipio", max_chars=50)

    #dato 18 (Sale asi en la tabla compartida por julian)
    nit_pagador = st.text_input("Nit del pagador. Sin digito de verificación", max_chars=9)

    #dato 19 (Sale asi en la tabla compartida por julian)
    fecha_ingreso = st.text_input("Fecha ingreso (AAAAMMDD)", max_chars=8)

    #dato 20 (Sale asi en la tabla compartida por julian)
    valor_mesada_pensional = st.text_input("Valor mesada pensional", max_chars=12)

    #dato 21 (Sale asi en la tabla compartida por julian)
    Tipo_excencion_gmf = st.selectbox("Tipo de Execion GMF: E = Exentas",["E"])

    #dato 22 (Sale asi en la tabla compartida por julian)
    cod_sucursal = st.text_input("Código Sucursal", max_chars=4)

    #dato 23 (Sale asi en la tabla compartida por julian)
    num_cuenta_preaperturada = st.text_input("Número de  Cuenta preaperturada Banco", max_chars=12, disabled=True)

    #dato 24 (Sale asi en la tabla compartida por julian)
    tipo_cuenta_respbanco = st.text_input("Tipo de cuenta", max_chars=2, disabled=True)


    if st.button("Generar linea 1 prepaertura "):
        
        linea_completa = funciones.preapertura(tipo_documento_preapertura,
                                               num_documento_prepaertura,
                                               primer_apellido_prepaertura,
                                               segundo_apellido_prepaertura,
                                               primer_nombre_prepaertura,
                                               segunda_nombre_prepaertura,
                                               Genero,
                                               fecha_nacimiento,
                                               direccion_pensionado,
                                               telefono_pensionado,
                                               celular_pensionado,
                                               codigo_dep_dane,
                                               nombre_dep,
                                               cod_ciudad_municipio_dane,
                                               nom_ciudad_municipio_dane,
                                               nit_pagador,
                                               fecha_ingreso,
                                               valor_mesada_pensional,
                                               Tipo_excencion_gmf,
                                               cod_sucursal,
                                               num_cuenta_preaperturada,
                                               tipo_cuenta_respbanco)
        
        st.session_state.preapertura.append(linea_completa)

st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.preapertura, 1):
    st.text(f"{linea}")

with st.expander("Registro control (linea 2)"):
    
    #dato 1
    nit_entidad_originadora_preapertura = st.text_input("Nit entidad originadora:", max_chars=12)

    #dato 2
    num_registros_total = st.text_input("Numero registros total", max_chars=8)

    #dato 3
    valor_total_preapertura = st.text_input("Valor total:", max_chars=18)

    #dato 4
    fecha_generacion_linea2 = st.text_input("Fecha generacion (AAAAMMDD)", max_chars=8)

    #dato 5
    hora_generacion_linea2= st.text_input("Hora generacion ( HHMMSS HH es la hora, MM es minuto y SS es segundo)", max_chars=6)


    if st.button("Generar linea 2 prepaertura "):
        
        linea_completa = funciones.preapertura2(nit_entidad_originadora_preapertura,
                                              num_registros_total,
                                              valor_total_preapertura,
                                              fecha_generacion_linea2,
                                              hora_generacion_linea2)
        
        st.session_state.preapertura.append(linea_completa)

st.write("📋Resultado:")
for i, linea in enumerate(st.session_state.preapertura, 1):
    st.text(f"{linea}")