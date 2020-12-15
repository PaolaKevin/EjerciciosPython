# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:43:07 2020

@author: cajamag
"""

concursantes = [{'nombre': 'Sebastian', 'sorteo': 5, 'puntaje': 15},
                 {'nombre': 'Maria', 'sorteo': 2, 'puntaje': 10},
                 {'nombre': 'Paula', 'sorteo': 1, 'puntaje': 3},
                 {'nombre': 'Samuel', 'sorteo': 4, 'puntaje': 20}
                 ]

def mostrar_vencedor(concursantes):
    vencedor = ''
    valorMasAlto = 0
    for d in concursantes:
        if d['puntaje'] > valorMasAlto:
            valorMasAlto = d['puntaje']
            vencedor = d['nombre']
    return vencedor, valorMasAlto

vencedor = mostrar_vencedor(concursantes)
nombre = vencedor[0]
puntos = vencedor[1]
print(f"El vencedor es {nombre} con {puntos} puntos")