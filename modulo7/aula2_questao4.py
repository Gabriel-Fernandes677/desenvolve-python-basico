import re

def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search(r"[A-Z]", senha):
        return False
    if not re.search(r"[a-z]", senha):
        return False
    if not re.search(r"[0-9]", senha):
        return False
    if not re.search(r"[@#$%^&+=!]", senha):
        return False
    return True
senha_usuario = input("Digite uma senha para validação: ")
    
if validador_senha(senha_usuario):
        print("A senha atende a todos os critérios.")
else:
        print("A senha não atende a todos os critérios.")
