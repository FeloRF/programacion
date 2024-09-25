#-*- coding: utf-8 -*-
# TI_M3_Actividad_1 Felipe Rojas ingenieria en informatica

"""
1.- Escribir un programa que lea entre 10 y 20 números ingresados por el usuario, los almacene
en una lista y los muestre ordenados de mayor a menor. El programa debe seguir recibiendo
ingreso de números hasta que el usuario ingrese 0. Sin embargo, el número 0 no debe ser
mostrado en pantalla.
1 Crear una lista vacía 
2 Precondicion: mientras el numero ingresado no sea "0" ni supere los 20 numeros.
    -pedir al usuario que ingrese un numero.
    -si el numero es "0" termina el bucle.
    -si el numero es diferente a "0" se agrega a la lista.
    -incrementar el contador de numeros
3 al ingresar 20 numeros, se detiene el ingreso, incluso que si no contiene el "0"
4 Crear una lista de los numeros.
5 Mostrar la lista ordenada de mayor a menor 
    """
    
# Se crea la lista
numeros = []

while True: 
    #El usuario ingresa un valor:
    numero =  int (raw_input("Ingresa un numero entre el 1 al 10 (0 para termianr): "))
    # si el numero es 0 y hay mas de 10 numeros, termina el bucle
    if numero == 0 and len(numeros)>=10:
        break
    # si se ingresa el 0 antes de tener 10 numeros, le pide al usuarios ingresar mas de 10 nemeros.
    elif numero == 0 and len(numeros)<10: 
        print ("Se debe tener al menos 10 numeros.")
        continue
    # Si ya estan los 20 numeros el bucle termia. 
    elif len(numeros) ==20:
        print("Se alacanzo el limite de 20 numeros.")
        break
    # Se agregan los valores a la lista, salvo el "0".
    else:
        numeros.append(numero)
# se orendenan los numeros
numero.sort(reverse=True)
# Se muestra la lista ordenada.
print("Los numeros ingresados y ordenados son: ", numeros)
    