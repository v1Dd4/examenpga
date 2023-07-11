

import numpy as np


tipodeps = ['A','B','C','D','a','b','c','d']
depa = 3800
depb = 3000
depc = 2800
depd = 3500
deptos_persona = []
arreglo_dpto = np.array([['A','B','C','D'],['A','B','C','D'],['A','B','C','D'],['A','B','C','D'],['A','B','C','D'],['A','B','C','D'],['A','B','C','D'],['A','B','C','D'],['A','B','C','D'],['A','B','C','D']])

def comprar_dep():
    for i in range(10):
        print(f'{i+1}.-{arreglo_dpto[i]}')
    selec = int(input('ingrese el numero de piso del dpto que desea comprar'))
    while selec > 10 or selec < 0:
        print('el piso del dpto no es valido porfavor intente denuevo')
        selec = int(input('ingrese el numero de piso del dpto que desea comprar'))
    tipo = input('ingrese el tipo de dpto que desea comprar')
    while tipo not in tipodeps:
        print('el tipo de dpto no es valido porfavor intente denuevo')
        tipo = input('ingrese el tipo de dpto que desea comprar')
    if check_dep(selec,tipo) == True:
        if tipo in ['a' , 'A']:
            arreglo_dpto[selec-1][0] = 'X'
            valor = depa
        elif tipo in ['b', 'B']:
            arreglo_dpto[selec-1][1] = 'X'
            valor = depb
        elif tipo in ['c' , 'C']:
            arreglo_dpto[selec-1][2] = 'X'
            valor = depc
        else:
            arreglo_dpto[selec-1][3] = 'X'
            valor = depd
        rut = input('ingrese el rut del comprador (CONSIDERE NO PONER NI PUNTOS NI GUION)\n')
        while len(rut) > 9 or len(rut) < 8:
            print('RUT NO VALIDO INGRESE UN RUT VALIDO')
            rut = input('ingrese el rut del comprador (CONSIDERE NO PONER NI PUNTOS NI GUION)\n')
        rut = rut[:len(rut)-1]
        comprador = [rut,f'{selec}{tipo}']
        deptos_persona.append(comprador)
    else: 
        print('dpto ya vendido')
    


def check_dep(selec,tipo):
    selec = selec-1
    if tipo in ['a' , 'A']:
        indice = 0
        if arreglo_dpto[selec][indice] == 'X':
            return False
        else:
            return True
    elif tipo in ['b', 'B']:
        indice = 1
        if arreglo_dpto[selec][indice] == 'X':
            return False
        else:
            return True
    elif tipo in ['c' , 'C']:
        indice = 2
        if arreglo_dpto[selec][indice] == 'X':
            return False
        else:
            return True
    elif tipo in  ['d','D']:
        indice = 3
        if arreglo_dpto[selec][indice] == 'X':
            return False
        else:
            return True
    


def disponibles():
    for i in range(10):
        print(f'{i+1}.-{arreglo_dpto[i]}')

def lista_compradores():
    print(deptos_persona)

def ver_ventas():
    conta = 0
    contb = 0
    contc = 0
    contd = 0
    for i in range(10):
        for j in range(4):
            if arreglo_dpto[i][j] == 'X':
                if j == 0:
                    conta = conta +1
                elif j == 1:
                    contb = contb +1
                elif j == 2:
                    contc = contc +1
                elif j == 3:
                    contd = contd +1
    print(F'''TIPO DPTO  -  CANTIDAD  -  TOTAL  
    TIPO A  -  {conta}  -  {conta*depa} UF
    TIPO B  -  {contb}  -  {contb*depb} UF
    TIPO C  -  {contc}  -  {contc*depc} UF
    TIPO D  -  {contd}  -  {contd*depd} UF
    TOTAL  -  {contd+conta+contb+contc}  -  {(conta*depa)+(contb*depb)+(contc*depc)+(contd*depd)} UF''')
