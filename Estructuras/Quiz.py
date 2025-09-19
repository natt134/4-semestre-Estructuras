def acumulador(n):
    resultado = None
    if n == 0:
        resultado = 0
    else:
        resultado = n + acumulador(n - 1)
        print({resultado})
    return resultado
n=int(input("ingrese un numero "))
acumulador(n)