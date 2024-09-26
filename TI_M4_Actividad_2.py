#-*- coding: utf-8 -*-
# TI_M4_Actividad_2 Felipe Rojas ingenieria en informatica

"""
 2.- se debe crear una función recursiva que lea números ingresados
por el usuario hasta que se ingrese un espacio en blanco. La función debe sumar los
números y devolver el resultado. Si el primer input es un espacio, la función debe imprimir
0  
    """
    
def sumar_numeros(suma_actual=0):
    # Pedir un número  
    entrada = raw_input("Ingresa un número (o presiona Enter para terminar): ")

    # Si el primer input es un espacio en blanco, devolver 0
    if entrada == "":
        return suma_actual

    # Convertir la entrada a un número y continuar la suma
    try:
        numero = float(entrada)  # Convertimos a float para manejar decimales
        return sumar_numeros(suma_actual + numero)  # Llamada recursiva sumando el número
    except ValueError:
        print("Por favor ingresa un número válido.")
        return sumar_numeros(suma_actual)  # Continuar pidiendo si no es un número

# Llamar a la función y mostrar el resultado
resultado = sumar_numeros()
print("La suma total de los números ingresados es:", resultado)
