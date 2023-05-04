#Ejercicio 3 insertar elementos y ordenarlos
#pedir numeros y meterlos en una lista, cuando el usuario introdusca un numero 0
#nuestro programa dejaria de insertar
lista = []
salir = False

while not salir:
    num = int(input('Digite un numero: '))
    if num == 0 :
        salir = True
    else:
        lista.append(num)
lista.sort() # La lista esta ordenada con esta funcion
print(f'\nla lista ordenada: \n{lista}')


