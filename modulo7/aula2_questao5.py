import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):

        if len(palavra) <= 3:
            return palavra
        
        primeiro = palavra[0]
        ultimo = palavra[-1]
        meio = list(palavra[1:-1])  
        
        random.shuffle(meio)
        
        return primeiro + ''.join(meio) + ultimo

    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    
    return ' '.join(palavras_embaralhadas)

frase_usuario = input("Digite uma frase: ")
    
nova_frase = embaralhar_palavras(frase_usuario)
    
print("Frase embaralhada:", nova_frase)

