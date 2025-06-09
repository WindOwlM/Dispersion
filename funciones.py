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
                     documento_ant):
    
    tipo_documento = tipo_documento
    
    documento = str(int(documento)).zfill(15)
    
    primer_apellido = str(primer_apellido).ljust(15,' ')
    segundo_apellido = str(segundo_apellido).ljust(15,' ')

    primer_nombre = str(primer_nombre).ljust(15,' ')
    segundo_nombre = str(segundo_nombre).ljust(15,' ')
    
    periodo_nomina = f"{periodo_nomina_anio}{periodo_nomina_mes:02d}"
    
    referencia = str(referencia).ljust(50,' ')
    
    banco = str(int(banco)).zfill(2)
    
    sucursal = str(int(sucursal)).zfill(4)
    
    cuenta = str(int(cuenta)).zfill(20)
    
    tipo_cuenta = tipo_cuenta
    
    valor_neto = str(int(valor_neto)).zfill(10)
    valor_neto = f"{valor_neto}00"
    
    tipo_documento_ant = tipo_documento_ant
    
    documento_ant = str(int(documento_ant)).zfill(15)
    
    linea_completa = f"{tipo_documento}{documento}{primer_apellido}{segundo_apellido}{primer_nombre}{segundo_nombre}{periodo_nomina}{referencia}{banco}{sucursal}{cuenta}{tipo_cuenta}{valor_neto}{tipo_documento_ant}{documento_ant}"
    
    return linea_completa