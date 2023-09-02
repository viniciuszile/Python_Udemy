"""
    Exercício
    Exiba os índices da lista 10/07/2023
"""

indice = 0
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))