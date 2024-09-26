#-*- coding: utf-8 -*-
# TI_M4_Actividad_1 Felipe Rojas ingenieria en informatica

"""
1.- Para el primer ejercicio, se debe crear una función que reciba una contraseña como
argumento y determine si es segura o no. Se deben implementar lógicas para verificar si
la contraseña contiene al menos una mayúscula, una minúscula y un número. La función
debe devolver True si es segura y False si no lo es    
    """
    
def es_segura(contrasena):
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    # Recorrer cada carácter en bsuca de numeros, mayusculas y minusculas
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True

    # Verificar si cumple todas las condiciones
    if tiene_mayuscula and tiene_minuscula and tiene_numero:
        return True
    else:
        return False

# Pedir al usuario que ingrese una contraseña
contrasena_usuario = raw_input("Ingresa una contraseña para verificar si es segura: ")

# Verificar si la contraseña es segura
if es_segura(contrasena_usuario):
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura. Debe contener al menos una mayúscula, una minúscula y un número.")
