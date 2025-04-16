import os
import re

def ler_salvar_palavras():
    # Nome do arquivo de entrada e saída
    arquivo_frase = "frase.txt"
    arquivo_palavras = "palavras.txt"

    # Verifica se o arquivo "frase.txt" existe
    if not os.path.exists(arquivo_frase):
        print(f"O arquivo '{arquivo_frase}' não foi encontrado.")
        return

    # Lê o conteúdo do arquivo "frase.txt"
    with open(arquivo_frase, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    # Remove espaços em branco e caracteres não alfabéticos
    # Usa regex para encontrar palavras que contêm apenas letras
    palavras = re.findall(r'[a-zA-ZÀ-ÿ]+', conteudo)

    # Salva as palavras em "palavras.txt"
    with open(arquivo_palavras, 'w', encoding='utf-8') as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + '\n')

    # Lê e imprime o conteúdo do arquivo "palavras.txt"
    with open(arquivo_palavras, 'r', encoding='utf-8') as arquivo:
        conteudo_palavras = arquivo.read()
        print("Conteúdo do arquivo 'palavras.txt':")
        print(conteudo_palavras)
ler_salvar_palavras()
