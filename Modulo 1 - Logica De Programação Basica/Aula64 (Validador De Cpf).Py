"""
    validador de cpf 10/07/2023
"""

cpf = "376.394.100-29".replace('.','').replace('-','').replace(' ','')
mult_regressivo1 = 10
mult_regressivo2 = 11
total_1 = 0
total_2 = 0

for index in range(9):
    
    int_numero = int(cpf[index])
    multiplicao =  int_numero * mult_regressivo1
    mult_regressivo1 -= 1
    
    total_1 = multiplicao + total_1
    
    index += 1
    
    if(index == 9):
        d1 = (total_1 * 10) % 11
        d1 = d1 if d1 <= 9 else 0
   
for index2 in range(10):
    
    int_numero = int(cpf[index2])
    
    multiplicao2 =  int_numero * mult_regressivo2
    mult_regressivo2 -= 1
    
    total_2 = multiplicao2 + total_2
    
    index2 += 1
    
    if(index2 == 10):
        d2 = (total_2 * 10) % 11
        d2 = d2 if d2 <= 9 else 0 
    
    
nove_digitos = cpf[:9]

cpf_gerado_pelo_calculo = f'{nove_digitos}{d1}{d2}'

if cpf == cpf_gerado_pelo_calculo:
    print(f'{cpf} é válido')
else:
    print('CPF inválido')


