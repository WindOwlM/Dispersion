def crear_dispersion(tipo_documento,
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
                     segundo_nombre_repre):
    
    tipo_documento = tipo_documento
    
    documento = str(documento).zfill(15)
    
    primer_apellido = str(primer_apellido).ljust(15,' ')
    segundo_apellido = str(segundo_apellido).ljust(15,' ')

    primer_nombre = str(primer_nombre).ljust(15,' ')
    segundo_nombre = str(segundo_nombre).ljust(15,' ')
    
    periodo_nomina = f"{periodo_nomina_anio}{periodo_nomina_mes:02d}"
    
    referencia = str(referencia).ljust(50,' ')
    
    banco = str(banco).zfill(2)
    
    sucursal = str(sucursal).zfill(4)
    
    cuenta = str(cuenta).zfill(20)
    
    tipo_cuenta = tipo_cuenta
    
    valor_neto = str(valor_neto).zfill(10)
    valor_neto = f"{valor_neto}00"
    
    tipo_documento_ant = tipo_documento_ant
    
    documento_ant = str(documento_ant).zfill(15)
    
    fecha_gen_mageti = fecha_gen_mageti.strftime('%Y%m%d')
    
    fecha_apli_pag = fecha_apli_pag.strftime('%Y%m%d')
    
    tipo_documento_repre = tipo_documento_repre
    
    documento_repre = str(documento_repre).zfill(15)
    
    primer_apellido_repre = str(primer_apellido_repre).ljust(15,' ')
    segundo_apellido_repre = str(segundo_apellido_repre).ljust(15,' ')

    primer_nombre_repre = str(primer_nombre_repre).ljust(15,' ')
    segundo_nombre_repre = str(segundo_nombre_repre).ljust(15,' ')
    
    linea_completa = f"{tipo_documento}{documento}{primer_apellido}{segundo_apellido}{primer_nombre}{segundo_nombre}{periodo_nomina}{referencia}{banco}{sucursal}{cuenta}{tipo_cuenta}{valor_neto}{tipo_documento_ant}{documento_ant}{fecha_gen_mageti}{fecha_apli_pag}{tipo_documento_repre}{documento_repre}{primer_apellido_repre}{segundo_apellido_repre}{primer_nombre_repre}{segundo_nombre_repre}."
    
    return linea_completa

def crear_linea_2(fecha_hora,
                  cantidad_total_registros,
                  valor_total_pagos,
                  cantidad_registros_abono_cuenta,
                  valor_total_abono,
                  cantidad_registros_pago_ventanilla,
                  valor_total_pago_ventanilla,
                  tipo_cuenta_dispersora,
                  numero_cuenta_dispersora,
                  tipo_identificacion_empresa_dispersora,
                  num_identificacion_empresa):
    
    cantidad_total_registros=str(cantidad_total_registros).zfill(8)
    valor_total_pagos = str(valor_total_pagos).zfill(16)
    valor_total_pagos = f"{valor_total_pagos}00"
    cantidad_registros_abono_cuenta=str(cantidad_registros_abono_cuenta).zfill(8)
    valor_total_abono = str(valor_total_abono).zfill(16)
    valor_total_abono = f"{valor_total_abono}00"
    cantidad_registros_pago_ventanilla=str(cantidad_registros_pago_ventanilla).zfill(8)
    valor_total_pago_ventanilla = str(valor_total_pago_ventanilla).zfill(16)
    valor_total_pago_ventanilla = f"{valor_total_pago_ventanilla}00"
    numero_cuenta_dispersora=str(numero_cuenta_dispersora).zfill(15)
    num_identificacion_empresa=str(num_identificacion_empresa).zfill(12)

   
    linea_completa = f"{fecha_hora}{cantidad_total_registros}{valor_total_pagos}{cantidad_registros_abono_cuenta}{valor_total_abono}{cantidad_registros_pago_ventanilla}{valor_total_pago_ventanilla}{tipo_cuenta_dispersora}{numero_cuenta_dispersora}{tipo_identificacion_empresa_dispersora}{num_identificacion_empresa}"
    
    return linea_completa

#De aqui para abajo es la funcion para las tablas de cupones
def cupones_1(cod_ent_bancaria,
              nom_ent_banco,
              cant_sucursal,
              cant_pensionados,
              anio_nomina,
              mes_nomina,
              fech_vence,
              mensaje):
    
    cod_ent_bancaria = str(cod_ent_bancaria).zfill(3)
    
    nom_ent_banco = str(nom_ent_banco).ljust(50,' ')
    
    cant_sucursal = str(cant_sucursal).zfill(4)
    
    cant_pensionados = str(cant_pensionados).zfill(7)
    
    anio_nomina = str(anio_nomina).zfill(4)
    
    mes_nomina = str(mes_nomina).zfill(2)
    
    fech_vence = str(fech_vence).zfill(10)
    
    mensaje = str(mensaje).ljust(250,' ')
    
    linea_completa = f"0{cod_ent_bancaria}{nom_ent_banco}{cant_sucursal}{cant_pensionados}{anio_nomina}{mes_nomina}{fech_vence}{mensaje}."
    
    return linea_completa

def cupones_2(num_cupon,
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
              nom_ciudad_sucursal):

    num_cupon = str(num_cupon).ljust(12,' ')
    
    num_documento_cupon_1 = str(num_documento_cupon_1).zfill(15)
    
    primer_apellido_cupon = str(primer_apellido_cupon).ljust(15,' ')
    segundo_apellido_cupon = str(segundo_apellido_cupon).ljust(15,' ')

    primer_nombre_cupon = str(primer_nombre_cupon).ljust(15,' ')
    segundo_nombre_cupon = str(segundo_nombre_cupon).ljust(15,' ')
    
    cod_sucursal_entidad = str(cod_sucursal_entidad).ljust(4,' ')
    
    nom_suc_ent_bancaria = str(nom_suc_ent_bancaria).ljust(25,' ')
    
    num_cuenta_cupon = str(num_cuenta_cupon).zfill(17)
    
    direc_sucursal = str(direc_sucursal).ljust(45,' ')
    
    cod_depart_dane = str(cod_depart_dane).zfill(2)
    
    nom_depart_sucursal = str(nom_depart_sucursal).ljust(50,' ')
    
    cod_ciudad_dane = str(cod_ciudad_dane).zfill(3)
    
    nom_ciudad_sucursal = str(nom_ciudad_sucursal).ljust(50,' ')
    
    linea_completa = f"1{num_cupon}{tipo_documento_cupon_1}{num_documento_cupon_1}{primer_apellido_cupon}{segundo_apellido_cupon}{primer_nombre_cupon}{segundo_nombre_cupon}{cod_sucursal_entidad}{nom_suc_ent_bancaria}{num_cuenta_cupon}{direc_sucursal}{cod_depart_dane}{nom_depart_sucursal}{cod_ciudad_dane}{nom_ciudad_sucursal}."

    return linea_completa

def cupones_3(tipo_documento_cupon_2,
              num_documento_cupon_2,
              tipo_movimiento,
              con_concept,
              nom_concept,
              var_concept):
    
    num_documento_cupon_2 = str(num_documento_cupon_2).zfill(15)
    
    con_concept = str(con_concept).zfill(5)
    
    nom_concept = str(nom_concept).ljust(40,' ')
    
    var_concept = str(var_concept).zfill(12)
    var_concept = f"{var_concept}00"
    
    linea_completa = f"2{tipo_documento_cupon_2}{num_documento_cupon_2}{tipo_movimiento}{con_concept}{nom_concept}{var_concept}"
    
    return linea_completa

def cupones_4(tipo_documento_cupon_3,
              num_documento_cupon_3,
              var_devenga,
              var_deducidos,
              var_neto,
              mensaje_per):
    
    num_documento_cupon_3 = str(num_documento_cupon_3).zfill(15)
    
    var_devenga = str(var_devenga).zfill(12)
    var_devenga = f"{var_devenga}00"
    
    var_deducidos = str(var_deducidos).zfill(12)
    var_deducidos = f"{var_deducidos}00"
    
    var_neto = str(var_neto).zfill(12)
    var_neto = f"{var_neto}00"
    
    mensaje_per = str(mensaje_per).ljust(250,' ')
    
    linea_completa = f"3{tipo_documento_cupon_3}{num_documento_cupon_3}{var_devenga}{var_deducidos}{var_neto}{mensaje_per}."
    
    return linea_completa

#De aqui para abajo es Ordenes de no pago

def Orden_no_pago(tipo_documento,
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
                  hora_pago):
     
     num_documento_onp = str(num_documento_onp).zfill(15)
     primer_apellido_onp = str(primer_apellido_onp).ljust(15,' ')
     segundo_apellido_onp = str(segundo_apellido_onp).ljust(15,' ')
     primer_nombre_onp = str(primer_nombre_onp).ljust(15,' ')
     segundo_nombre_onp = str(segundo_nombre_onp).ljust(15,' ')
     referencia_onp = str(referencia_onp).zfill(50)
     sucursal_banco = str(sucursal_banco).zfill(4)
     cuenta_onp = str(cuenta_onp).zfill(20)
     Valor_neto_onp = str(Valor_neto_onp).zfill(12)
     fecha_fallecimiento = str(fecha_fallecimiento).zfill(8)
     descripcion_causal_np = str(descripcion_causal_np).ljust(150,' ')
     respuesta_banco = str(respuesta_banco).ljust(1,' ')
     valor_reintegro = str(valor_reintegro).ljust(12,' ')
     desc_causal_np_banco = str(desc_causal_np_banco).ljust(150,' ')
     causal_np_banco = str(causal_np_banco).ljust(4,' ')
     fecha_pago_reintegro = str(fecha_pago_reintegro).ljust(8,' ')
     hora_pago = str(hora_pago).ljust(5,' ')
     

     linea_completa = f"{tipo_documento}{num_documento_onp}{primer_apellido_onp}{segundo_apellido_onp}{primer_nombre_onp}{segundo_nombre_onp}{periodo_nomina_onp}{referencia_onp}{codigo_banco}{sucursal_banco}{cuenta_onp}{tipo_cuenta_onp}{Valor_neto_onp}{estado_pago}{fecha_onp}{fecha_fallecimiento}{descripcion_causal_np}{respuesta_banco}{valor_reintegro}{desc_causal_np_banco}{causal_np_banco}{fecha_pago_reintegro}{hora_pago}."
     
     return linea_completa

def Orden_no_pago2(nit_entidad_originadora,
                   num_registros_total,
                   valor_total,
                   fecha_generacion,
                   hora_generacion):
     
     nit_entidad_originadora = str(nit_entidad_originadora).zfill(12)
     num_registros_total = str(num_registros_total).zfill(8)
     valor_total = str(valor_total).zfill(16)
     valor_total = f"{valor_total}00"

     

     linea_completa = f"{nit_entidad_originadora}{num_registros_total}{valor_total}{fecha_generacion}{hora_generacion}."
     
     return linea_completa


#De aqui para abajo es preapertura

def preapertura(tipo_documento_preapertura,
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
                nit_pagador):
     
     num_documento_prepaertura = str(num_documento_prepaertura).zfill(15)
     primer_apellido_prepaertura = str(primer_apellido_prepaertura).ljust(15,' ')
     segundo_apellido_prepaertura = str(segundo_apellido_prepaertura).ljust(15,' ')
     primer_nombre_prepaertura = str(primer_nombre_prepaertura).ljust(15,' ')
     segunda_nombre_prepaertura = str(segunda_nombre_prepaertura).ljust(15,' ')
     direccion_pensionado = str(direccion_pensionado).ljust(45,' ')
     telefono_pensionado = str(telefono_pensionado).zfill(7)
     celular_pensionado = str(celular_pensionado).zfill(10)
     codigo_dep_dane = str(codigo_dep_dane).zfill(2)
     nombre_dep = str(nombre_dep).ljust(50,' ')
     cod_ciudad_municipio_dane = str(cod_ciudad_municipio_dane).zfill(3)
     nom_ciudad_municipio_dane = str(nom_ciudad_municipio_dane).ljust(50,' ')
     nit_pagador= str(nit_pagador).zfill(9)

     linea_completa = f"{tipo_documento_preapertura}{num_documento_prepaertura}{primer_apellido_prepaertura}{segundo_apellido_prepaertura}{primer_nombre_prepaertura}{segunda_nombre_prepaertura}{Genero}{fecha_nacimiento}{direccion_pensionado}{telefono_pensionado}{celular_pensionado}{codigo_dep_dane}{nombre_dep}{cod_ciudad_municipio_dane}{nom_ciudad_municipio_dane}{nit_pagador}."
     
     return linea_completa