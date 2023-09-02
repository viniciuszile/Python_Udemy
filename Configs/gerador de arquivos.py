i = 25


while True:
    i += 1

    with open(f'aula{i}.py', 'w') as arquivo:
        arquivo.write("aula nao realizada")

    if i == 100:
        break

print("Arquivos criados com sucesso!")


