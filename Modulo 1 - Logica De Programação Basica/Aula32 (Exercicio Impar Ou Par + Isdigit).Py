#Exercicios 16/06/2023


"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input("informe um numero inteiro: ")

if entrada.isdigit():
    entrada_int = int(entrada)

    if(entrada_int % 2 == 0):
        impar_par = "par"
    else:
        impar_par = "impar"

    print(f'O número {entrada_int} é {impar_par}')
else:
    print('Você não digitou um número inteiro')
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input("Digite as horas: ")

horas = int(entrada)

if(horas >= 0) and (horas < 12):
    print("bom dia !!")
elif(horas >= 12) and (horas < 18):
    print("boa tarde !!")
else:
    print("boa noite !!!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("escreva seu nome: ")

if(len(nome) < 4):
    print("seu nome é curto")
elif(len(nome) > 6):
    print("seu nome é muito grande!")
else:
    print("seu nome é normal.")