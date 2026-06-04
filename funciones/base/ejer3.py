def promedio_total (cant_notas, suma_notas):
    prom = suma_notas/cant_notas
    return prom
def analisis_prom (promedio):
    if promedio>= 7 and promedio<=10:
        print("APROBADO")
    elif promedio<7 and promedio>=0:
        print("DESAPROBADO")
    else:
        print("PROMEDIO IMPOSIBLE")
cant= 0
notas = 0
while True:
    nota= float(input("Ingresa tu nota: "))
    if nota>10 and nota<0:
        print("La nota tiene que ser del 1 al 10")
    else:
        cant +=1
        notas += nota
    salir = int(input("Apreta 1 para salir y 2 para seguir: "))
    if salir !=2 :
        break
promedio = promedio_total(cant, notas)
analisis_prom(promedio)