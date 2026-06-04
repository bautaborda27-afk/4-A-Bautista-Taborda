def padel (luz, socio):
    base = 10000
    if luz == True and socio == True:
        total = base+2000-(base*10/100)
        print("PRECIO A PAGAR: ", total)
    elif luz == True and socio == False:
        total = base+ 2000
        print("PRECIO A PAGAR: ", total)
    else:
        print("PRECIO A PAGAR: ", base)
sos = input("Responde por si o no. Eres socio?:")
soc = sos.lower()== "si"
sos2 = input("Responde por si o no. Utilizaste la luz?: ")
luz= sos2.lower()== "si"
padel(luz, soc)
