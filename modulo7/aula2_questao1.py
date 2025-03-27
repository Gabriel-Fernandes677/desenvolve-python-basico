data_nascimento = input("Digite a sua data de nascimento (dd/mm/aaaa): ")

    # Divide a data em dia, mês e ano
dia, mes, ano = data_nascimento.split('/')

    # Lista com os meses do ano por extenso
meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    # Converte o mês de string para inteiro
mes_numero = int(mes)

    # Obtém o nome do mês correspondente
if 1 <= mes_numero <= 12:
        mes_extenso = meses[mes_numero - 1]  # -1 para ajustar ao índice da lista
        # Imprime a data formatada
        print(f"Sua data de nascimento é: {dia} de {mes_extenso} de {ano}.")
else:
        print("Mês inválido! Por favor, insira um mês entre 01 e 12.")
