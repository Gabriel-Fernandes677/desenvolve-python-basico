def calcular_primeiro_digito(cpf):
    soma = 0
    multip = 10 
    for digito in cpf[:9]:
        soma += int(digito) * multip
        multip -= 1
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def calcular_segundo_digito(cpf, primeiro_digito):
    soma = 0
    multip = 11 
    for digito in cpf[:9] + str(primeiro_digito):
        soma += int(digito) * multip
        multip -= 1
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    primeiro_digito = calcular_primeiro_digito(cpf)
    segundo_digito = calcular_segundo_digito(cpf, primeiro_digito)

    return cpf[-2] == str(primeiro_digito) and cpf[-1] == str(segundo_digito)

cpf_input = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")

if validar_cpf(cpf_input):
    print("Válido")
else:
    print("Inválido")
