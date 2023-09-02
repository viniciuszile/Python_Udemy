# Problema dos parâmetros mutáveis em funções Python

#funcao que cria listar individuais e retorna elas na varivel que chamou a função
def cria_lista(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


nomes = cria_lista('Vinicius')
cria_lista('janaina', nomes)
cria_lista('Jessica', nomes)
nomes.append('Pedro')

frutas = cria_lista('Banana')
cria_lista('Maça', frutas)

obtejos = cria_lista('Bola')
cria_lista('livro', obtejos)

print(nomes)
print(frutas)
print(obtejos)