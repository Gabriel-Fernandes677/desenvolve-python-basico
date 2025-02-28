Idade = int(input("Digite sua idade: "))
Jogos = bool(input("Já jogou pelo menos 3 jogos de tabuleiro? "))
Vitorias = int(input("Quantos jogos ja venceu? "))
resultado = Idade >= 16 or Idade <= 18 and Jogos >= 3 and Vitorias >=1
print(f"Apto para ingressar no clube de jogos de tabuleiro: {resultado}")









