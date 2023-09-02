# Exercícios copy, sorted, produtos.sort
# 

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
import pprint


def p(v):
    pprint.pprint(v, sort_dicts=False, width=40,)
    
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.10}
    for produto in produtos
]

lista = copy.deepcopy(novos_produtos)

print("Aumente os preços dos produtos a seguir em 10%")
p(lista)
print()


# 
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(lista, key=lambda x: x['nome'], reverse=True)

copia_produtos_ordenados = copy.deepcopy(produtos_ordenados_por_nome)

print("Ordene os produtos por nome decrescente (do maior para menor)")
p(copia_produtos_ordenados)
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(lista, key=lambda x: x['preco'], reverse=False)

copia_produtos_ordenados_p = copy.deepcopy(produtos_ordenados_por_preco)

print("Ordene os produtos por preco crescente (do menor para maior)")
p(copia_produtos_ordenados_p)
print()


