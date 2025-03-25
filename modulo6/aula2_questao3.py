import random
from collections import Counter

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]
intersecao = list(set(lista1) & set(lista2))
intersecao.sort()

contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção ordenada:", intersecao)

print("\nQuantidade de vezes que cada elemento aparece em cada lista:")
print("Lista 1:")
for numero in contagem_lista1:
    print(f"{numero}: {contagem_lista1[numero]} vez(es)")

print("\nLista 2:")
for numero in contagem_lista2:
    print(f"{numero}: {contagem_lista2[numero]} vez(es)")
