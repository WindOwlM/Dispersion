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

def crear_linea_2(fecha_hora):
    

  
    
    linea_completa = f"{fecha_hora}"
    
    return linea_completa