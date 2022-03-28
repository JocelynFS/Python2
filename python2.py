import random

def sumaArreglo(arreglo):
    i=0
    for elemento in arreglo:
        i += elemento
    return i

def arregloal(tamaño):
    arreglo = random.sample(range(100), tamaño)
    print(arreglo)
    return arreglo

def arregloman(tamaño):
    arreglo = []
    for x in range(tamaño):
        valor = int(input('Ingrese el valor: '))
        arreglo.append(valor)
    return arreglo

def tamañoarr(tamaño):
    if tamaño > 1000:
        print('Se excedió el tamaño del arreglo.')
        n = int(input('Ingrese otro tamaño del arreglo: '))
    else:
        n = tamaño
    return n

print('Función para sumar un arreglo.')
while True:
    print('Digite la forma en la que quiere obtener su arreglo')
    opcion = int(input('1. Manualmente \n2. Aleatoriamente \n0. Salir \n'))
    if opcion == 0:
        print('Adiós...')
        break
    elif opcion == 1:
        tamaño = int(input('Digite el tamaño del arreglo: '))
        tamaño = tamañoarr(tamaño)
        arreglo = arregloman(tamaño)
        print(f'La suma es: {sumaArreglo(arreglo)}')
    elif opcion == 2:
        tamaño = int(input('Digite el tamaño del arreglo: '))
        tamaño = tamañoarr(tamaño)
        arreglo = arregloal(tamaño)
        print(f'La suma es: {sumaArreglo(arreglo)}')
    else:
        print('Opción inválida')









"""print('Digite la forma en la que quiere obtener su arreglo')
opcion = int(input('1. Manualmente \n 2. Aleatoriamente \n 0. Salir'))
tamaño = int(input('Digite el tamaño del arreglo: '))
if opcion == 1:
    arreglo = arregloman(tamaño)
    print(sumaArreglo(arreglo))
elif opcion == 2:
    arreglo = arregloal(tamaño)
    print(sumaArreglo(arreglo))
else:
    print('Opción inválida')"""
