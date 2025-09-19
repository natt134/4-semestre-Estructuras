# Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario
# indique al inicio del programa.


def llenar_fibonacci():
    n = int(input("¿Cuántos números de la serie de Fibonacci quieres generar? "))
    while n <= 0:
        n = int(input("Por favor ingresa un número mayor a 0: "))

    lista = []

    if n >= 1:
        lista.append(0)  
    if n >= 2:
        lista.append(1)  

    for i in range(2, n):
        siguiente = lista[i-1] + lista[i-2]
        lista.append(siguiente)

    return lista


print(" Serie de Fibonacci \n")

fibonacci = llenar_fibonacci()

print(f"➡️ La serie de Fibonacci generada es: {fibonacci}")
