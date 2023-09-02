'''
    Sets são eficientes para remover valores duplicados
    de iteráveis.
    Seus valores serão sempre únicos;
    Não aceitam valores mutáveis;
    não tem índexes;
    não garantem ordem;
    são iteráveis (for, in, not in)
'''

l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
s1 = {1, 2, 3}

print(3 not in s1)

for numero in s1:
    print(numero)
