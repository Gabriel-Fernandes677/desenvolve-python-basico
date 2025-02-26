valor = int(input("Digite o valor: "))

nota100 = valor // 100
valor = valor % 100

nota50 = valor // 50
valor = valor % 50

nota20 = valor // 20
valor = valor % 20

nota10 = valor // 10
valor = valor % 10

nota5 = valor // 5
valor = valor % 5

nota2 = valor // 2
valor = valor % 2

nota1 = valor // 1

# Saída formatada
print("Notas:")
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")
