#-*- coding: utf-8 -*-
# TI_M3_Actividad_3.2 Felipe Rojas ingenieria en informatica
"""
Construir un programa en donde el usuario ingrese números por pantalla y el programa
devuelva la suma de todos los números ingresados por el usuario. Si el usuario ingresa un
carácter no numérico, el programa debe mostrar un mensaje de error y continuar
solicitando números y sumando. El programa finaliza cuando el usuario presione enter
    
    """
    
# Contador numeros 
suma_total = 0

# Bucle para recivir los numeros 
while True:
    # Solicita número 
    entrada = raw_input("Ingresa un número (o presiona Enter para finalizar): ")
    
    # Verificar si el usuario presionó Enter sin ingresar algun valor
    if entrada == "":
        break
    
    # Convierte los datos ingresados en numeros flotamtes (hacepta numeros decimales)
    try:
        numero = float(entrada)  
        suma_total += numero     # Sumar el número a la suma total
    except ValueError:
        # Si ingresa una letra no genera error sino que muestra el mensaje 
        print("Error: Ingresa un número válido.")
        continue

# muestra la suma total de los números 
print("La suma total de los números ingresados es:", suma_total)
