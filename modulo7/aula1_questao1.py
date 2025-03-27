def escada_nome(nome):

    for i in range(1, len(nome) + 1):
        print(nome[:i])
nome_usuario = input("Por favor, insira seu nome: ")
escada_nome(nome_usuario)

