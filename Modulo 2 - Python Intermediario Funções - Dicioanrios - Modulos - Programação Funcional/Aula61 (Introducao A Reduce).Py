# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 1},
    {'nome': 'Produto 1', 'preco': 2},
    {'nome': 'Produto 3', 'preco': 3},
    {'nome': 'Produto 2', 'preco': 4},
    {'nome': 'Produto 4', 'preco': 5},
]


def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']


total = reduce(
    funcao_do_reduce,
    produtos,
    0
)

print('Total é', total)