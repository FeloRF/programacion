#-*- coding: utf-8 -*-
# TI_M3_Actividad_3 Felipe Rojas ingenieria en informatica

"""
 3.- ¡Juguemos Scrabble! Construye un diccionario con los siguientes valores. Luego, el usuario
ingresa una palabra por pantalla y el programa devuelve el puntaje correspondiente.  
1) A E I L N O R S T U
2 )D G
3) B C M P
4) F H V W Y
5) k
8) J X
10)Q Z
 
    """
    
#1.- Aprender como se juega Scrabble!. 

# Diccionario con letras y sus valores. 
valores_letras = {
    1: "A E I L N O R S T U",
    2: "D G",
    3: "B C M P",
    4: "F H V W Y",
    5: "K",
    8: "J X",
    10: "Q Z"
}

# Crear un diccionario inverso donde las letras sean las claves y los puntos los valores
puntos_letra = {}

# Llenar el diccionario inverso
for puntos, letras in valores_letras.items():
    for letra in letras.split():
        puntos_letra[letra] = puntos

# Solicitar una palabra al usuario
palabra = raw_input("Ingresa una palabra: ").upper()

# Inicializar el puntaje en 0
puntaje_total = 0

# Calcular el puntaje sumando el valor de cada letra
for letra in palabra:
    puntaje_total += puntos_letra.get(letra, 0)  # Sumar 0 si la letra no está en el diccionario

# Mostrar el puntaje total
print("El puntaje de la palabra ingresada es:", puntaje_total)
