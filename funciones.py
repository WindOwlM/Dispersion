def crear_dispersion(tipo_documento,documento):
    
    tipo_documento = tipo_documento
    
    documento = str(int(documento)).zfill(15)
    
    linea_completa = f"{tipo_documento}{documento}"
    
    return linea_completa