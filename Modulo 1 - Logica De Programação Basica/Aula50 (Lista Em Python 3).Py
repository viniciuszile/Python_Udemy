"""
    Listas em Python 10/07/2023
    Tipo list - Mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis:
        append - Adiciona um item ao final
        insert - Adiciona um item no índice escolhido
        pop - Remove do final ou do índice escolhido
        del - apaga um índice
        clear - limpa a lista
        extend - estende a lista
        + - concatena listas
    Create Read Update   Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('zile') #insere no final da lista
nome = lista.pop() #remove o ultimo elemento da lista

lista.append(1233) #insere no final da lista
del lista[-1] #deleta o ultimo item da lista

# lista.clear() #limpa a lista
# print(lista) printa a lista vazia


lista.insert(3, "costa") # adiciona o elemento no index informado 
print(lista, lista[4])