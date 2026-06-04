def calcular_recargo (monto_actual, metodo_pago):
    if metodo_pago.lower() == "tarjeta":
        dsc = monto_actual * 0.10
        recargo = monto_actual - dsc 
        print("El monto a pagar con tarjeta es: ", monto_actual)
        print("El recargo que tienes por pagar con tarjeta es de: ", recargo)
    if metodo_pago.lower() == "efectivo":
        dsc = monto_actual * 0.15
        monto_actual -= dsc 
        print("El monto a pagar con efectivo es: ", monto_actual)
    if metodo_pago.lower() == "transferencia":
        print("Tu moto a pagar es de: ", monto_actual)

    return monto_actual

        