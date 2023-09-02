#Aula sobre prints. 12/06/2023

"""
    CRLF = \r\n ou \n usado de forma "escondida" como padrão para quebrar a linha automaticamente.
    sep = "" -> usado para formatar a separação dos argumentos(espaço é o padrão.)
    end = "" -> usado para formartar o final do print(quebra de linha é o padrão.)
"""

argumento1 = "olá"
argumento2 = 123

print(argumento1, argumento2) #print sem nenhuma formatação
print(argumento1, argumento2, sep="//") #print usando // como separação inves do espaço
print(argumento1, argumento2, end="##") #print usando ## no final da linha inves da quebra de linha como padrão

