''''
    Coerção de tipos (converter um tipo em outro) 14/06/2023
    conversão de tipos, coerção
    type convertion, typecasting, coercion
    é o ato de converter um tipo em outro
    tipos imutáveis e primitivos:
    str, int, float, bool
'''
# Coerção de str para int
str_number = '10'  # Declaração de uma string contendo um número
integer_number = int(str_number)  # Conversão da string para um número inteiro usando a função int()
print(integer_number)  # Exibição do número inteiro resultante

# Coerção de str para float
str_number = '3.14'  # Declaração de uma string contendo um número de ponto flutuante
float_number = float(str_number)  # Conversão da string para um número de ponto flutuante usando a função float()
print(float_number)  # Exibição do número de ponto flutuante resultante

# Coerção de str para bool
str_value = 'True'  # Declaração de uma string contendo um valor booleano
bool_value = bool(str_value)  # Conversão da string para um valor booleano usando a função bool()
print(bool_value)  # Exibição do valor booleano resultante

# Coerção de int para str
integer_number = 42  # Declaração de um número inteiro
str_number = str(integer_number)  # Conversão do número inteiro para uma string usando a função str()
print(str_number)  # Exibição da string resultante
