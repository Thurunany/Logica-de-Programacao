def limparString(originalString):
    ''''
    params originalString: uma string de entrada, que pode possuir números ou caracteres especiais
    returns: uma string que contenha apenas os números, sem os caracteres especiais.
    '''
    finalString = ''
    for caracter in originalString:
        if caracter.isdigit():
            finalString += caracter
    return finalString


def verificarTamanho(originalString):
    '''
    params originalString: Uma string que deve ser um CPF
    returns: True se a originalString possui 11 dígitos (considerando apenas números).
    '''
    stringLimpa = limparString(originalString)
    return len(stringLimpa) == 11

def digito_10(cpf):
    '''
    params cpf: Uma string digitado, representa o CPF
    returns: o décimo digito, se cpf tem tamanho igual a 11
    '''
    cpf_limpo = limparString(cpf)
    if verificarTamanho(cpf_limpo):
        i = 10
        soma = 0
        while i >= 2:
            soma = soma + (i * int(cpf_limpo[10 - i]))
            i = i -1
        resto = soma % 11
        if resto == 1 or resto == 0:
            return '0'
        else:
            return str(11 - resto)

def digito_11(cpf):
    '''
    params cpf: Uma string digitado, representa o CPF
    returns: o décimo primeiro digito, se cpf tem tamanho igual a 11
    '''
    cpf_limpo = limparString(cpf)
    if verificarTamanho(cpf_limpo):
        i = 11
        soma = 0
        while i >= 2:
            soma = soma + (i * int(cpf_limpo[11 - i]))
            i = i -1
        resto = soma % 11
        if resto == 1 or resto == 0:
            return '0'
        else:
            return str(11 - resto)

def verificarCPF(cpf):
    cpf = limparString(cpf)
    digito10 = digito_10(cpf)
    digito11 = digito_11(cpf)
    if digito10 and digito11:
        return cpf[9:] == digito10 + digito11
    return False
