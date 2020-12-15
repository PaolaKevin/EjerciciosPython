# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 23:06:15 2020

@author: cajamag
"""
def contarElementosLista(lista):
    """
    Recibe una lista, y devuelve un diccionario con todas las repeticiones de
    cada valor
    """
    return {i:lista.count(i) for i in lista}
 
lista = ["a", "c", "b", "a", "c", "c", "a", "c"]
resultado=contarElementosLista(lista) # {'a': 3, 'b': 1, 'c': 3}
maximo=max(resultado, key=resultado.get)
print("El valor mas repetido es el ",maximo," con ",resultado[maximo]," veces")
 
 
lista = [1,2,3,2,1,4,2,5,2,4,2,3]
resultado=contarElementosLista(lista) # {1: 2, 2: 5, 3: 2, 4: 2, 5: 1}
maximo=max(resultado, key=resultado.get)
print("El valor mas repetido es el ",maximo," con ",resultado[maximo]," veces")