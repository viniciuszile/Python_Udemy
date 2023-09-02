'''
    Introdução ao for / in 10/07/2023
'''

texto = 'Python'

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')