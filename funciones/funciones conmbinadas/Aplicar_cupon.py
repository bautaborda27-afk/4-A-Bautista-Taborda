def aplicar_cupon (monto_total, codigo_cupon):
    if codigo_cupon.lower() == "proa2026":
        dsc = monto_total*0.15
        monto_total -= dsc
        print("El total con este descuento: ", codigo_cupon, ". Es del 15% el resultado final a pagar es de: ", monto_total)
    elif codigo_cupon.lower() == "proaproa":
        dsc = monto_total*0.25
        monto_total -= dsc
        print("El total con este descuento: ", codigo_cupon, ". Es del 25% el resultado final a pagar es de: ", monto_total)
    elif codigo_cupon.lower() == "belgrano":
        dsc = monto_total*0.50
        monto_total -= dsc
        print("El total con este descuento: ", codigo_cupon, ". Es del 50% el resultado final a pagar es de: ", monto_total)
    else:
        print("Codigo de descuento no valido")

    
    return monto_total