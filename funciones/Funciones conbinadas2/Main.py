from absoluto_precio import *
from costo import *
from cupones import *
from Elección import *
from recargo import *
from stock import *
from PUNTOS import *
from envio import *
from ticket import *

elec = elección()
cant = stock(elec)
cost_total = costo(elec, cant)
print("Ingresa la a cuantos KM te ubicas")
cant_KM = int(input())
cost_envio = calcular_envio(cant_KM)
cupon_ing = input("Ingresa el cupon: ")
costo_con_cupon = cupon(cost_total, cupon_ing)
metodo_pago = input("Ingresa el metodo de pago que quieres utilizar: ")
costo_final = calcular_recargo(costo_con_cupon, metodo_pago)
costo_con_envio = costo_final+cost_envio
puntos_adquiridos = calcular_puntos(costo_con_envio)
ticket (costo_final, cost_envio, costo_con_envio, puntos_adquiridos)