"""
    Cuidados com dados mutáveis 10/07/2023
    = - copiado o valor (imutáveis)
    = - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['zile', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)