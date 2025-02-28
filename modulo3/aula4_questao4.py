Distancia = int(input("Digite a distância: "))
Peso = int(input("Digite o peso do pacote: "))
valor = 0
if Distancia  <=100:
    valor = Peso
if Distancia > 101 and Distancia < 300:
    valor = Peso * 1.50
if Distancia > 300:
    valor = Peso * 2
if Peso > 10:
    valor = valor + 10
print(f"O Valor do frete será de: {valor}")


