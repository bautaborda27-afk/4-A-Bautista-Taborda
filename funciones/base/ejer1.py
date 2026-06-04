def precio_final (precio):
    iva = precio*21/100
    print("Ingresa el descuento que quiera. Apreta 0 si no hay descuento ")
    dsc = float (input())
    desctotal = precio*dsc/100
    if dsc < 0 and dsc > 100:
        print("No hay descuento..")
        total = precio+iva
    else:
        total= precio+iva-desctotal
        print("El total de la compra es de:",total)

print("Ingresa el valor de los productos: ")
pre = float(input())
precio_final(pre)