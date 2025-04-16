def processar_arquivo():
    # Nome do arquivo
    nome_arquivo = "estomago.txt"

    try:
        # Abre o arquivo para leitura
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # Lê todas as linhas do arquivo
            linhas = arquivo.readlines()

            # 1. Imprime o texto das primeiras 25 linhas
            print("Primeiras 25 linhas do roteiro:")
            for linha in linhas[:25]:
                print(linha.strip())

            # 2. Conta o número total de linhas no arquivo
            numero_linhas = len(linhas)
            print("\nNúmero total de linhas do arquivo:", numero_linhas)

            # 3. Encontra a linha com maior número de caracteres
            linha_maior = max(linhas, key=len)
            print("Linha com maior número de caracteres:")
            print(linha_maior.strip())

            # 4. Contar mencões aos personagens "Nonato" e "Íria"
            # Usar expressões regulares para contar as variações de "Nonato" e "Íria"
            import re
            cont_nonato = sum(1 for linha in linhas if re.search(r'\bNonato\b', linha, re.IGNORECASE))
            cont_iria = sum(1 for linha in linhas if re.search(r'\bÍria\b', linha, re.IGNORECASE))

            print("\nNúmero de menções a 'Nonato':", cont_nonato)
            print("Número de menções a 'Íria':", cont_iria)

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        
processar_arquivo()
