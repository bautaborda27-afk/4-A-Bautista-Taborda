def cuadrados (numero):
    total = 0
    for i in range(1, numero+1):
        res = i**2
        total += res
    
    print("El resultado es: ",total)
print("ingresa el numero:")
num = int(input())
cuadrados(num)