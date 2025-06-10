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