def contar_espacos(frase):
    return frase.count(' ')  
frase = input("Por favor, insira uma frase: ")
    
numero_de_espacos = contar_espacos(frase)
    
print(f"A frase contém {numero_de_espacos} espaços em branco.")

