# Desempacotamento em chamadas 10/07/2023
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

p, b, *_, ap, u = lista
print(p, u, ap)

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista, sep=" -- ")
print(*string,sep=" - ")
print(*tupla, sep=" ")

print(*salas, sep='\n')