quant1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {quant1} elementos da lista 1:")
lis1 = []

for _ in range(quant1):
    num = int(input())
    lis1.append(num)

quant2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {quant2} elementos da lista 2:")
lis2 = []

for _ in range(quant2):
    num = int(input())
    lis2.append(num)
 
inter = []

min_length = min(len(lis1), len(lis2))

for i in range(min_length):
    inter.append(lis1[i])
    inter.append(lis2[i])

if len(lis1) > len(lis2):
    inter.extend(lis1[min_length:])
else:
    inter.extend(lis2[min_length:])

print(inter)
