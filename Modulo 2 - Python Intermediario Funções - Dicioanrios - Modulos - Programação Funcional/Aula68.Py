caminho_arquivo = "aula68.txt"

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.remove(caminho_arquivo) # ou unlink # exclui o arquivo
# os.rename(caminho_arquivo, 'aula68-2.txt') # renomea o arquivo