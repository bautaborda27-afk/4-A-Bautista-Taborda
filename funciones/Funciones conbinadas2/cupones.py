def cupon (total, codigo_cupon):
    if codigo_cupon.lower() == "proa2026":
        dsc = total*0.15
        monto_total -= dsc
        print("El total con este descuento: ", codigo_cupon, ". Es del 15% el resultado final a pagar es de: ", total)
    elif codigo_cupon.lower() == "proaproa":
        dsc = total*0.25
        total -= dsc
        print("El total con este descuento: ", codigo_cupon, ". Es del 25% el resultado final a pagar es de: ", total)
    elif codigo_cupon.lower() == "belgrano":
        dsc = total*0.50
        total -= dsc
        print("El total con este descuento: ", codigo_cupon, ". Es del 50% el resultado final a pagar es de: ", total)
    else:
        print("Codigo de descuento no valido")

    
    return total