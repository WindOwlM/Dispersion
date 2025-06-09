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
                     sucursal):
    
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
    
    linea_completa = f"{tipo_documento}{documento}{primer_apellido}{segundo_apellido}{primer_nombre}{segundo_nombre}{periodo_nomina}{referencia}{banco}{sucursal}"
    
    
    return linea_completa