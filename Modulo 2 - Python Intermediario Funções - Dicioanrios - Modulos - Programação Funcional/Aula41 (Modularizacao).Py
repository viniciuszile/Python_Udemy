# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path



print('Este módulo se chama', __name__)

teste = input("digite 1 para acessar o outro arquivo")

if(teste == "1"):
    import Aula41_m
else:
    print("nao entrei no outro arquivo")