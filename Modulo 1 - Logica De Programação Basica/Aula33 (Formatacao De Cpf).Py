"""
    21/06/2023
    https://docs.python.org/pt-br/3/library/stdtypes.html
    Imutáveis que vimos: str, int, float, bool
"""

cpf = '50780879018'
cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'


print("" + cpf_formatado)

# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)
# print(string.zfill(10))