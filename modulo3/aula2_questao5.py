Gen = input("Digite seu gênero: ")
Idade = int(input("Digite sua idade: "))
Tempo = int(input("Tempo de serviço: "))
print(f"Pode aposentar: {Gen=='F' and Idade >= 60 or Gen=='M' and Idade >=65  or Tempo >=30 or Idade >=60 and Tempo >=25 }")



