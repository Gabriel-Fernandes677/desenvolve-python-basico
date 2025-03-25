frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

lista_vogais = sorted([letra for letra in frase if letra in vogais])
print("Vogais na frase (ordenadas):", lista_vogais)

lista_consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais]
print("Consoantes na frase (sem espaços):", lista_consoantes)
