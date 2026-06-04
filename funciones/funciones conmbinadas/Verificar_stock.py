def verificar_stock(cantidad_solicitada):
    stock=10

    if cantidad_solicitada >stock:
            print("Stock no disponible")
    elif cantidad_solicitada <= stock:
            print("Hay stock disponible, se te entregara la mercaderia")
            stock -= cantidad_solicitada

    while cantidad_solicitada != -1:
        cantidad_solicitada = int(input("Cuantas piezas necesitas?:"))
        if cantidad_solicitada >stock:
                print("Stock no disponible")
        elif cantidad_solicitada <= stock:
                print("Hay stock disponible, se te entregara la mercaderia")
                stock -= cantidad_solicitada
        


        

