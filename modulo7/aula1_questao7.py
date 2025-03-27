import random

def encrypt(strings):
    n = random.randint(1, 10)
    strings_criptografadas = []

    for s in strings:
        criptografada = ""
        for c in s:

            novo_codigo = ord(c) + n
            if novo_codigo > 126:  
            
                novo_codigo = 33 + (novo_codigo - 127)
            criptografada += chr(novo_codigo)
        strings_criptografadas.append(criptografada)

    return strings_criptografadas, n
    
lista_de_strings = ["Hello, World!", "Python", "Encrypt this!"]
strings_criptografadas, chave = encrypt(lista_de_strings)
    
print("Chave de criptografia:", chave)
print("Strings criptografadas:", strings_criptografadas)

