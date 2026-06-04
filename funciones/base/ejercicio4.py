#Bautista Taborda
saldo = 1500
papas = 500
gase = 800
seguir = True
opc  = 0
while seguir == True:
    print("Selecciona una opcion:")
    print("1- Papas Fritas ($500)")
    print("2- Gaseosa ($800)")
    print("3- Ver Saldo")
    print("4- Salir")
    opc = int(input())
    if opc == 1 :
        if saldo >= papas:
            print ("Expulsando papas")
            saldo -= papas
        else:
            print("Saldos insuficientes")
    elif opc == 2:
        if saldo >= gase:
            print("Expulsando gaseosa")
            saldo -= gase
        else:
            print("Saldos insuficientes")
    elif opc == 3:
        print("Tu saldo es de ", saldo)
    elif opc == 4:
        if saldo == 0:
            print("Gracias por comprar")
            seguir = False
        else:
            print("Tu vuelto es de ", saldo, ". GRACIAS")
            seguir = False


        

    