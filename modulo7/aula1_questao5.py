def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    indices_vogais = []
    contador_vogais = 0

    for i, letra in enumerate(frase):
        if letra in vogais:
            indices_vogais.append(i)
            contador_vogais += 1

    return contador_vogais, indices_vogais
    
frase = input("Digite uma frase: ")
    
total_vogais, indices = contar_vogais(frase)

print(f"A frase contém {total_vogais} vogais.")
if total_vogais > 0:
    print("Os índices das vogais são:", indices)
