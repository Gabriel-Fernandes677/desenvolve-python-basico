n = int(input("Quantidade de respondentes: "))
cont = 0 
idade = 0
while cont<n:
    idade += int(input("Digite a idade: "))
    cont += 1
print(f"Media das idades de {n} respondentes = {idade/n}")


