def formatar_celular(numero):
  
    numero = ''.join(filter(str.isdigit, numero))
    
    if len(numero) == 8:
        
        numero = '9' + numero
    elif len(numero) == 9:
        if numero[0] != '9':
            return "Número inválido. Um número com 9 dígitos deve começar com 9."
    else:
        return "Número inválido. O número deve ter 8 ou 9 dígitos."

    return f"{numero[:5]}-{numero[5:]}"
    
numero_celular = input("Digite um número de celular (8 ou 9 dígitos): ")

resultado = formatar_celular(numero_celular)
print("Número formatado:", resultado)
