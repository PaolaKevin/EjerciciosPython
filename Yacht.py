# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:28:16 2020

@author: cajamag
"""

import random

def rollDice(caras, cantidad, tiradas):
    rolls = [0] * caras
    for i in range(0, tiradas):
        roll_1 = int(random.randint(1,caras))
        roll_2 = int(random.randint(1,caras))
        resultado = roll_1 + roll_2
        rolls[resultado - 1] += 1
    return rolls

if __name__ == "__main__":
    caras = int(input("Inserte la cantidad de caras por dado: "))
    cantidad = int(input("\nInserte la cantidad de dados: "))
    tiradas = int(input("\nInserte la cantidad de tiradas: "))

    result = rollDice(caras, cantidad, tiradas)
    print(result[1:])