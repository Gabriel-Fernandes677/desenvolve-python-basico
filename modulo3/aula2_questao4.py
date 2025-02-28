Classe = input("Qual a classe do personagem: ")
For = int(input("Pontos de força: "))
Mp = int(input("Pontos de magia: "))
Resultado = Classe == "mago" and For <=10 and Mp >=15 or Classe == "guerreiro" and For>=15 and Mp <=10 or Classe == "arqueiro" and For > 5 and For <=15 and Mp >5 and Mp <=15  
print(f"Pontos de atributo consistentes com a classe escolhida: {Resultado}")







