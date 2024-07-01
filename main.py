# Centro de Biotecnologia Agropecuaria
# Fecha: 13/06/24
# Aprendiz: Daniel Alexander Duarte Ussa
# Ficha: 2877795
# Version: 3.12.2


from calculos import *
from listas import *



# Funcion donde se imprimen las listas, suma y promedio de la lista general
def main():
    while True:
        try:

            # Random List es la lista 'General'
            randomList = generate_random_list()

            # Even List(Numeros pares) y Odd List(Numeros impares) es la lista donde se guardaran los numeros pares de la lista general
            evenList, oddList = separate_even_odd(randomList)

            # Llamamos la funcion calculos, 
            total, promedio = calculos(randomList)

            print("Lista generada:", randomList)
            print("La lista tiene", len(randomList), "elementos")
            print("La suma de todos los números es:", total)
            print("El promedio de la lista es:", promedio)
            print("Los números pares son:", evenList)
            print("Los números impares son:", oddList)

            m = continuar_listas()

            if m == 'no':
                exit()
            main()
        except ValueError as e:
            print(f'Error: {e}')

if __name__ == "__main__":
    main()