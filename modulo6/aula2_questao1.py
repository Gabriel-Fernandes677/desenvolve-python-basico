from random import randint

lista = []
for i in range(0,20):
    lista.append(randint(-100,100))
ordenada = sorted(lista)
print(f"Ordenada: {ordenada}")
print(f"Original: {lista}")
print(f"Indice maior valor da lista: {lista.index(max(lista))}")
print(f"Indice menor valor da lista: {lista.index(min(lista))}") 
