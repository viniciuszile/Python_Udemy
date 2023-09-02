"""
    15/06/2023
    CONSTANTE = "Variáveis" que não vão mudar
    Muitas condições no mesmo if (ruim)
        <- Contagem de complexidade (ruim)
"""


# Exemplo de Constante
PI = 3.14159  # Definição da constante PI
raio = 5  # Definição do raio do círculo
area = PI * (raio ** 2)  # Cálculo da área do círculo usando a constante PI
print(area)  # Exibição da área do círculo

# Exemplo de Muitas condições no mesmo if
nota = 80  # Definição da nota do aluno

if nota >= 90:  # Verificação da condição: nota maior ou igual a 90
    print('A')
elif nota >= 80:  # Verificação da condição: nota maior ou igual a 80
    print('B')
elif nota >= 70:  # Verificação da condição: nota maior ou igual a 70
    print('C')
elif nota >= 60:  # Verificação da condição: nota maior ou igual a 60
    print('D')
else:  # Se nenhuma das condições anteriores for verdadeira
    print('F')

# Exemplo de Contagem de complexidade
num = 7  # Definição do número

if num > 0 and num % 2 == 0 and num % 3 == 0:  # Verificação de múltiplas condições
    print('Número é positivo, divisível por 2 e 3')
else:
    print('Número não atende às condições')
