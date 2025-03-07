QExper = int(input("Quantidade de experimentos: ")) 
total = 0
sapo = 0
rato =0
coelho = 0

while total<QExper:
    cob,quant = input("Cobaia Utilizada[S:sapo,R:rato,C:coelho]: "),int(input("Quantidade: "))
    total += quant
    if cob == "C":
        coelho += quant 
    elif cob == "R":
        rato += quant
    elif cob == "S":
        sapo += quant
        print(sapo)

perCo = (coelho/total)*100
perRa = (rato/total)*100
perSa = (sapo/total)*100

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {perCo}%")
print(f"Percentual de ratos: {perRa}%")
print(f"Percentual de sapos: {perSa}%")





