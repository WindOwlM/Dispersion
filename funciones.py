def crear_dispersion(tipo_documento,documento,primer_apellido,segundo_apellido,primer_nombre,segundo_nombre):
    
    tipo_documento = tipo_documento
    
    documento = str(int(documento)).zfill(15)
    
    linea_completa = f"{tipo_documento}{documento}"
    
    primer_apellido = str(primer_apellido).ljust(15,' ')
    segundo_apellido = str(segundo_apellido).ljust(15,' ')

    primer_nombre = str(primer_nombre).ljust(15,' ')
    segundo_nombre = str(segundo_nombre).ljust(15,' ')
    
    return linea_completa