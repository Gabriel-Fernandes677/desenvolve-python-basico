import string

def eh_palindromo(frase):

    frase_normalizada = frase.translate(str.maketrans('', '',string.punctuation)).replace(" ", "").lower()
    
    return frase_normalizada == frase_normalizada[::-1]
while True:
        # Solicita ao usuário que insira uma frase
        frase_usuario = input("Digite uma frase (ou 'Fim' para encerrar): ")
        
        # Verifica se o usuário deseja encerrar o programa
        if frase_usuario.lower() == "fim":
            break
        
        # Verifica se a frase é um palíndromo
        if eh_palindromo(frase_usuario):
            print("A frase é um palíndromo.")
        else:
            print("A frase não é um palíndromo.")
