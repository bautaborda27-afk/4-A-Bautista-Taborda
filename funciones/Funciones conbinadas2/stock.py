def stock (elec):
    pen_stock = 7
    funda_stock = 5
    carga_stock = 10
    if elec == 1:
        print("Que cantidad de productos quieres? Solo hay ", pen_stock, "en stock")
        ped = int(input("Pedido:"))
        if ped > pen_stock:
            print("Stock no disponible")
        elif ped <= pen_stock:
            print("Stock disponible")
            return ped
    elif elec == 2:
        print("Que cantidad de productos quieres? Solo hay ", funda_stock, "en stock")
        ped = int(input("Pedido:"))  
        if ped > funda_stock:
            print("Stock no disponible")
        elif ped <= funda_stock:
            print("Stock disponible")
            return ped  
    elif elec == 3:
        print("Que cantidad de productos quieres? Solo hay ", carga_stock, "en stock")
        ped = int(input("Pedido:"))
        if ped > carga_stock:
            print("Stock no disponible")
        elif ped <= carga_stock:
            print("Stock disponible")
            return ped
    else:
        print("Opcion erroñea")
    