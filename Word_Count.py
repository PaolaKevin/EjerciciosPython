# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 05:24:58 2020

@author: cajamag
"""

cadenaPalabras = 'Mi mamá me ama, mi mamá me mima'


listaPalabras = cadenaPalabras.split()

cantidad = []
for w in listaPalabras:
    cantidad.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(cantidad) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, cantidad))))