from collections import Counter

def encontrar_anagramas(string, palavra_objetivo):
    tamanho_palavra = len(palavra_objetivo)
    contagem_objetivo = Counter(palavra_objetivo)
    anagramas_encontrados = []

   
    for i in range(len(string) - tamanho_palavra + 1):
    
        substring_atual = string[i:i + tamanho_palavra]
        contagem_atual = Counter(substring_atual)
        
        
        if contagem_atual == contagem_objetivo:
            anagramas_encontrados.append(substring_atual)

    return anagramas_encontrados
    
string = input("Digite a string: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
    
anagramas = encontrar_anagramas(string, palavra_objetivo) 
   
if anagramas:
    print("Anagramas encontrados:", anagramas)
else:
    print("Nenhum anagrama encontrado.")
