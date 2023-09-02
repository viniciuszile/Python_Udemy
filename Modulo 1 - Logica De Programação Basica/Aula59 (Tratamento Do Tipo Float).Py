"""
    Imprecisão de ponto flutuante 10/07/2023
    Double-precision floating-point format IEEE 754
    https://en.wikipedia.org/wiki/Double-precision_floating-point_format
    https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
    """
import decimal

numero_1 = decimal.Decimal('0.1') #para usar da maneira correta a "funcao" Decimal, deve informar o numero como str
numero_2 = decimal.Decimal('0.7') #para usar da maneira correta a "funcao" Decimal, deve informar o numero como str

numero_3 = numero_1 + numero_2

print(numero_3)

print(f'{numero_3:.2f}') #formata a string para um determinado numero de casas
print(round(numero_3, 2)) #arredonda o numero

numero_arredondado = (round(numero_3, 1))

print(f"numero 3 arrendondado {numero_arredondado}")