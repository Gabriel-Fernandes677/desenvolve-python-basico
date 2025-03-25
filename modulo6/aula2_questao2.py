from random import randint

num_elementos = randint(5,20)
elementos = []
for i in range(1,num_elementos):
    elementos.append(randint(1,10))
print("Lista:",elementos)
print("Soma dos valores da lista: ",sum(elementos))
print(f"Média dos valores da lista: {(sum(elementos)/len(elementos))}")
