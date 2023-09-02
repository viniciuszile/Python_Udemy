import os
from unidecode import unidecode

def padronizar_nome_arquivos(diretorio):
    for nome_arquivo in os.listdir(diretorio):
        nome_sem_acentos = unidecode(nome_arquivo)
        palavras = nome_sem_acentos.split()  # Divide o nome em palavras
        palavras_capitalizadas = [palavra.title() for palavra in palavras]
        novo_nome = " ".join(palavras_capitalizadas)
        
        if nome_arquivo != novo_nome:
            antigo_caminho = os.path.join(diretorio, nome_arquivo)
            novo_caminho = os.path.join(diretorio, novo_nome)
            
            os.rename(antigo_caminho, novo_caminho)
            print(f"Renomeado: {nome_arquivo} -> {novo_nome}")

# Obtém o caminho absoluto do diretório onde o script está
diretorio_script = os.path.dirname(os.path.abspath(__file__))

padronizar_nome_arquivos(diretorio_script)