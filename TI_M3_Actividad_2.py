#-*- coding: utf-8 -*-
# TI_M3_Actividad_2 Felipe Rojas ingenieria en informatica

"""
2.- Escribir un programa que almacene palabras ingresadas por el usuario. El programa debe
seguir recibiendo ingreso de palabras hasta que el usuario ingrese tres asteriscos "***". Luego
de esto, las palabras deben ser mostradas por pantalla una única vez. Es decir, si el usuario
ingresó palabras repetidas, solo se deben mostrar una vez.
    
    """
# Inicializar una lista para almacenar palabras
palabras = []

# Bucle para recibir las palabras
while True:
    # Solicitar palabra al usuario
    palabra = raw_input("Ingresa una palabra (*** para terminar): ")
    
    # Verificar si el usuario ingresó tres asteriscos para terminar
    if palabra == "***":
        break
    
    # Verificar si el usuario ingresó más de una palabra
    if " " in palabra:
        print("Solo se permite ingresar una palabra a la vez. Intenta nuevamente.")
        continue
    
    # Agregar la palabra a la lista si aún no está en ella para evitar duplicados
    if palabra not in palabras:
        palabras.append(palabra)

# Mostrar las palabras ingresadas en una sola línea, manteniendo el orden de ingreso
print("Palabras ingresadas sin repetir:")
for palabra in palabras:
    print palabra,
