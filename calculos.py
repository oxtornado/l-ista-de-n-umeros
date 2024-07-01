# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2


from listas import *

# Funcion para la suma de todos los elementos de la lista junto a su promedio
def calculos(elementos_de_la_lista):

    # Suma de todos los elementos
    # Forma larga:
    total = 0

    for i in elementos_de_la_lista:
        total = total + i
    
    # Forma corta:
    # total = sum(elementos_de_la_lista)

    # Creacion la variable promedio
    promedio = total / len(elementos_de_la_lista)

    # Al terminar, devolver los valores respectivamente
    return total, promedio

