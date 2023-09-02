"""
    Listas em Python 10/07/2023
    Tipo list - Mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis:
        append, insert, pop, del, clear, extend, +
    Create Read Update   Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
lista.append(50) #adiciona o 50 no final da lista

print(lista)

lista.pop() # remove o ultimo elemento da lista

print(lista)

valor = lista.pop(0)
print(lista, 'Removido,', valor)