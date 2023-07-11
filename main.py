import os
import time
from funciones import comprar_dep,disponibles,lista_compradores,ver_ventas

run = True
while run:
    print('bienvenido a casa feliz')
    print('1)COMPRAR UN DPTO')
    print('2)VER DPTOS DISPONIBLES')
    print('3)VER LISTA DE COMPRADORES')
    print('4)VER VENTAS TOTALES')
    print('5)SALIR')

    op = int(input('INGRESE SU OPCION'))
    if op == 1:
        comprar_dep()
    elif op == 2:
        disponibles()
    elif op == 3:
        lista_compradores()
    elif op == 4:
        ver_ventas()
    else:
        run = False
        print('SALIENDO               DAVID DIAZ 10/07/2023')



