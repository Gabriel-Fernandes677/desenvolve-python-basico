import random

def ler_palavras(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return [linha.strip() for linha in f.readlines()]

def ler_enforcado(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return [linha.strip() for linha in f.readlines()]

def imprime_enforcado(erros, enforcado):
    for i in range(erros + 1):
        print(enforcado[i])

def jogo_da_forca():
    palavras = ler_palavras("gabarito_forca.txt")
    enforcado = ler_enforcado("gabarito_enforcado.txt")

    palavra = random.choice(palavras)
    letras_adivinhadas = []
    tentativas = 6
    erros = 0

    print("Bem-vindo ao Jogo da Forca!")
    print("_ " * len(palavra))

    while erros < tentativas:
        letra = input("Adivinhe uma letra: ").lower()
        
        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_adivinhadas.append(letra)

        if letra in palavra:
            print("Você acertou uma letra!")
        else:
            erros += 1
            print("Você errou! Tentativas restantes:", tentativas - erros)

        progresso = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])
        print("Palavra: " + ' '.join(progresso))


        imprime_enforcado(erros, enforcado)

        if '_' not in progresso:
            print("Parabéns! Você acertou a palavra:", palavra)
            break
    else:
        print("Você foi enforcado! A palavra era:", palavra)
        
jogo_da_forca()
