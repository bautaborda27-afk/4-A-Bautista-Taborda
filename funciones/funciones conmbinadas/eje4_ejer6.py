from Verificar_stock import *
from Calcular_envio import *
from Aplicar_cupon import *
from Calcular_recargo import *
from Calcular_puntos import *
from Ticket import *
def ticket (costo_total, costo_envio, subtotal, puntosganados ):
    print("_______________________________________________________")
    print("_______________________________________________________")
    print("Subtotal: ", subtotal)
    print("Costo de envio: ", costo_envio)
    print("Total a pagar: ", costo_total)
    print("Puntos a ganar: ", puntosganados)
    print("_______________________________________________________")
    print("_______________________________________________________")

print("Hola!! cuantas unidades necesitas?")
unid = int(input())
verificar_stock(unid)

print("A cuantos kilometros del local te ubicas?")
kmdis = float(input())
envio = calcular_envio(kmdis)

print("Cual fue el costo total de la compra?")
cost = float(input())
cupon = input("Ingresa tu cupon: ")
costo_cupones = aplicar_cupon(cost,cupon)


metodo = input("Elegi el metodo de pago: ")
total = calcular_recargo(costo_cupones ,metodo)

puntos = calcular_puntos(total)

ticket(costo_cupones + envio, envio, cost , puntos)