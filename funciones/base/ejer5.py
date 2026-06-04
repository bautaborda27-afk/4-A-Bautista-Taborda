
def tabla (numero):
    res=0
    for i in range(1,11):
        res = i *numero
        print(numero,"X", i,"=", res)
print("La tabla de que numero quieres que saquemos: ")
num=float(input())
tabla(num)
