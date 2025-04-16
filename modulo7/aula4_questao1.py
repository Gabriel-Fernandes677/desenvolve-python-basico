import os

def salvar_frase():

    frase_usuario = input("Digite uma frase: ")
    
    nome_arquivo = "frase.txt"

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(frase_usuario)

    caminho_completo = os.path.abspath(nome_arquivo)

    print("Frase salva em:", caminho_completo)
salvar_frase()
