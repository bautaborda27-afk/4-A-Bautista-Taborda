
def suma (n1,n2):
    sumadenum = n1 + n2
    print(sumadenum)
    return sumadenum
def resta (n1, n2):
    if n1 > n2:
        restadenum = n1 - n2
    elif n1 < n2:
        restadenum = n2-n1
    else:
        restadenum = 0
    print(restadenum)
    return restadenum
def multiplicación(n1, n2):
    multidenum = n1 * n2
    print(multidenum)
    return multidenum
def dividir(n1,n2):
    if n2 != 0:
        dividenum = n1/n2
    else:
        dividenum = "NO SE PUEDE DIVIDIR POR 0"
    print(dividenum)
    return dividenum
def promedio (n1, n2):
    sumdenum_prome = n1 + n2
    divicion_prome = sumdenum_prome/2
    print(divicion_prome)
    return divicion_prome
def porcentaje(n1,n2):
    mult_porcentaje = n1*n2
    div_porcentaje = mult_porcentaje/100
    print(div_porcentaje)
    return div_porcentaje
def menu():
    op =int(input("Ingresa la opción. Presiona 1(sumar) 2(Restar) 3(Multiplicar) 4(Dividir) 5(Promedio) 6(Porcentaje) 0(SALIR): "))
    return op
while True:
    opc = menu()
    if opc == 1:
        num1= float(input("Ingresa el numero: "))
        num2= float(input("Ingresa el numero: "))
        suma(num1, num2)
    elif opc == 2:
        num1= float(input("Ingresa el numero: "))
        num2= float(input("Ingresa el numero: "))
        resta(num1, num2)
    elif opc == 3:
        num1= float(input("Ingresa el numero: "))
        num2= float(input("Ingresa el numero: "))
        multiplicación(num1, num2)
    elif opc == 4:
        num1= float(input("Ingresa el numero: "))
        num2= float(input("Ingresa el numero: "))
        dividir(num1, num2)
    elif opc == 5:
        num1= float(input("Ingresa el numero: "))
        num2= float(input("Ingresa el numero: "))
        promedio(num1, num2)
    elif opc == 6:
        num1= float(input("Ingresa el numero: "))
        num2= float(input("Ingresa el numero: "))
        porcentaje(num1, num2)
    else:
        print("Gracias!!")
        break
