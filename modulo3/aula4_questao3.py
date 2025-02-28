Ano = int(input("Digite um ano: "))

if Ano%4 == 0 and Ano%100 != 0 or Ano%400 == 0:
    print("bissexto")
else:
    print("não bissexto")


