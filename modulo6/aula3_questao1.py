

numeros = []

while True:
        try:
            num = int(input("Digite um número inteiro (ou 'sair' para finalizar): "))
            numeros.append(num)
 
            if len(numeros) >= 4:
                continuar = input("Deseja adicionar mais números? (s/n): ")
                if continuar.lower() == 'n':
                    break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

print("\nLista original:", numeros)

print("Os 3 primeiros elementos:", numeros[:3])

print("Os 2 últimos elementos:", numeros[-2:])

print("Lista invertida:", numeros[::-1])

print("Elementos de índice par:", numeros[::2])

print("Elementos de índice ímpar:", numeros[1::2])


