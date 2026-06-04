
def calcular_envio (distancia_km):
    costo_envio = 2000
    if distancia_km<=5:
        print("El costo del envio es de ",costo_envio)
    elif distancia_km>5:
        restn = distancia_km-5
        result = restn*500
        costo_envio += result
        print("El costo del envio es de ",costo_envio)      
    return costo_envio
