
numeros_pares = [num for num in range(20, 51) if num % 2 == 0]
print("Números pares entre 20 e 50:", numeros_pares)

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [valor ** 2 for valor in valores]
print("Quadrados dos valores:", quadrados)

numeros_divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]
print("Números entre 1 e 100 divisíveis por 7:", numeros_divisiveis_por_7)

paridade = ['par' if num % 2 == 0 else 'impar' for num in range(0, 30, 3)]
print("Paridade dos números em range(0,30,3):", paridade)
