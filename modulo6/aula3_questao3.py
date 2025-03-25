import random

lista = [random.randint(-10, 10) for _ in range(20)]

print("Lista original:", lista)


max_negativos = 0
melhor_inicio = 0
melhor_fim = 0


for i in range(len(lista)):
    for j in range(i, len(lista)):
        sub_lista = lista[i:j+1]
        negativos_count = sum(1 for num in sub_lista if num < 0)
        
        if negativos_count > max_negativos:
            max_negativos = negativos_count
            melhor_inicio = i
            melhor_fim = j


del lista[melhor_inicio:melhor_fim+1]

print("Lista após deleção do intervalo com mais negativos:", lista)
