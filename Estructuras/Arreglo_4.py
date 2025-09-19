# Llenar un arreglo de n elementos con números generados con la función random. No
# puede haber números repetidos. Si intenta ingresar al arreglo un número que ya existe,
# imprimirlo para anunciar que ese número ya está en el arreglo.

import random

def llenar_sin_repetidos():
    n = int(input("¿Cuántos números quieres en el arreglo? "))
    while n <= 0:  # si el usuario pone 0 o negativo, vuelve a pedir
        n = int(input("Por favor ingresa un número mayor a 0: "))

    lista = []
    intentos = 0

    while len(lista) < n:
        numero = random.randint(1, 100)  
        intentos += 1
        if numero in lista:
            print(f"El número {numero} ya está en el arreglo (ignorado)")
        else:
            lista.append(numero)
            print(f"Número {numero} agregado al arreglo")

    print(f"\nArreglo final sin repetidos ({len(lista)} elementos): {lista}")
    print(f"Intentos realizados para llenarlo: {intentos}")

    return lista

print("Generando un arreglo con números aleatorios sin repetidos...\n")
arreglo = llenar_sin_repetidos()
