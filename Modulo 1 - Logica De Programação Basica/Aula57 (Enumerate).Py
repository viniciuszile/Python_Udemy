"""
    enumerate - enumera iteráveis (índices) 10/07/2023
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


for indice, nome in enumerate(lista):
    print(indice, nome)



