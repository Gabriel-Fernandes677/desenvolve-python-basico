from random import randint
from math import sqrt

soma = 0
n = int(input("Digite um valor: "))
for i in range(0,n):
    rand = randint(0,100)
    soma += rand
print(f"Raiz quadrada da soma de {n} valores aleatórios: ",sqrt(soma))




