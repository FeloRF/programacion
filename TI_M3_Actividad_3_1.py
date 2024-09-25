#-*- coding: utf-8 -*-
# TI_M3_Actividad_3.1 Felipe Rojas ingenieria en informatica

# Se define la comparacion de las palabras y cuantas veces aparecen 
def contar_letras(palabra):
    contador = {}
    for letra in palabra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador

# Solicitar las palabras al usuario
palabra1 = raw_input("Ingresa la primera palabra: ").lower()
palabra2 = raw_input("Ingresa la segunda palabra: ").lower()

# Contar las letras de ambas palabras
contador_palabra1 = contar_letras(palabra1)
contador_palabra2 = contar_letras(palabra2)

# Comparar los diccionarios de letras
if contador_palabra1 == contador_palabra2:
    print("Las palabras son anagramas.")
else:
    print("Las palabras no son anagramas.")
