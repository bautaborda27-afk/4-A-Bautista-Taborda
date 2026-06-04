def calcular_puntos (monto_final_abonado):
    
    puntos = monto_final_abonado//1000*5
    if puntos >50:
        puntos = 50
    return puntos
