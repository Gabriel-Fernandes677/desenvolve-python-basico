def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    
    for vogal in vogais:
        frase = frase.replace(vogal, "*")
    
    return frase
 # Solicita ao usuário que insira uma frase
frase_usuario = input("Digite uma frase: ")
    
    # Chama a função para substituir as vogais
frase_substituida = substituir_vogais(frase_usuario)
    
    # Imprime a frase com as vogais substituídas
print("Frase com vogais substituídas:", frase_substituida)

