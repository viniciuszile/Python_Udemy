""" Calculadora com while 07/07/2023 """
while True:
    
    res = 0
    operadores_permitidos = '+-/*'
    
    
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    else:
        if(operador == "+"):
            res = num_1_float + num_2_float
        elif(operador == "-"):
            res = num_1_float - num_2_float
        elif(operador == "*"):
            res = num_1_float * num_2_float
        elif(operador == "/"):
            res = num_1_float / num_2_float

    print("o resultado da operação")
    print(f"{num_1_float} {operador} {num_2_float} = {res}")

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break