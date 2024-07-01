# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2


import random

# Generacion de lista hasta que el numero 0 aparezca en el rango
def generate_random_list():

    # Creacion de lista
    randomList = []

    # Bucle para que siga generando numeros dentro de la lista
    while True:

        # Variable que asigna un rango de numeros para agregar a la lista
        n = random.randint(0, 20)

        # Condicion para seguir agregando numeros a la lista
        if n == 0:
            #Finalizar bucle si el numero generado es 0
            break

        # De lo contrario, agregar la lista
        randomList.append(n)

    # Retorne la lista con los numeros aleatorios generados
    return randomList

# Separacion de los numeros pares dentro la lista 'general'
def separate_even_odd(elementos_de_la_lista):

    # Creacion de las listas que van a contener los numeros
    # Pares
    evenList = []

    #Impares
    oddList = []

    # Bucle para que vaya recorriendo uno por uno los elementos de la lista
    for n in elementos_de_la_lista:

        #Condicion donde si el residuo de la division del numero entre dos es cero lleva a ser par
        if n % 2 == 0:

            # Al ser par, se agregara a la lista de numero pares, o 'EvenList'
            evenList.append(n)

        # De lo contrario, se tomara como numero impar
        else:
            # Funcion 'append' para ir agregando estos elementos a la lista
            oddList.append(n)
    return evenList, oddList


def continuar_listas():
    while True:
        resp = input('Desea continuar generando listas aleatorias?: ')
        if resp != 'no':
            break
        elif resp == 'no':
            print('Hasta luego.')
            exit()
    return resp