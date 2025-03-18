from random import randint
vl = randint(1,10)
while True:
    ad = int(input("Adivinhe um número entre 1 e 10: "))
    if ad == vl:
        print(f"Correto! O número é {vl}.")
        break
    elif ad < vl:
        print("Baixo, tente novamente!")
    elif ad > vl:
        print("Alto, tente novamente!")








