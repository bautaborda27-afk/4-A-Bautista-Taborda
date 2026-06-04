def calcular_puntos (monto_final_abonado):
    puntos = monto_final_abonado//1000
    if puntos*5 <= 50: 
        print("Los puntos que obtuviste: ", puntos*5)
        return puntos*5
    else:
        print("Los puntos que obtuviste: 50",)
        return 50