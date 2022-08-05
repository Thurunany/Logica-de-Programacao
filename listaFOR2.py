def troca_caixa(texto):
    '''
    :param texto: um texto em formato string, para ser convertido
    :returns: um novo texto, convertido conforme a regra a seguir.

    Deve retornar um novo texto em que as vogais ficam em caixa alta (maiúsculas)
    e as consoates ficam em caixa baixa (minúsculas)

    OBS: Não pode ser utilizado o método replace() da classe string.
    Dica: Crie uma nova string (vazia) e percorra a string 'texto'. 
    Verifique se cada caracter é uma vogal, e grave na nova string o caracter
    em maiúsculo ou minúsculo, conforme a o caso.

    Exemplo:
    - texto: Eu amo estudar no IFC.
    - Deve retornar:
           EU AmO EstUdAr nO Ifc.
    '''

    tamanho = len(texto)
    texto = texto.lower()
    texto_novo = ('')
    
    for thuaninha in range(tamanho):
        if texto[thuaninha] == 'a':
            texto_novo += texto[thuaninha].upper()
        elif texto[thuaninha] == 'e':
            texto_novo += texto[thuaninha].upper()
        elif texto[thuaninha] == 'i':
            texto_novo += texto[thuaninha].upper()
        elif texto[thuaninha] == 'o':
            texto_novo += texto[thuaninha].upper()
        elif texto[thuaninha] == 'u':
            texto_novo += texto[thuaninha].upper()           
        else:
            texto_novo += texto[thuaninha]
    return texto_novo
    

def numero_legal(numero):
    '''
    params numero: um numero em formato string.
    returns: um valor boolean (True ou False), conforme regra a seguir.

    Se a soma dos dígitos do número for par, retorne True, pois isso é legal.
    Caso contrário, retorne False.

    Dica: Note que o número já está em formato string
    
    Exemplo:
      numero = 3467 -> True, pois 3+4+6+7 = 20 (que é par)
      numero = 1235 -> False, pois 1+2+3+5 = 11 (que é ímpar)
    '''
    lista_de_numero = []
    for a in numero:
        a = int(a)
        lista_de_numero.append(a)
    if sum(lista_de_numero) % 2 == 0:
        return True
    else:
        return False

def numero_chato(numero):
    '''
    params numero: um numero em formato string.
    returns: um valor boolean (True ou False), conforme regra a seguir.

    Não pode haver dois dígitos consecutivos idênticos, porque isso é chato.
    Se tiverem dois número consectivos, retorne True. Caso contrário, retorne False.

    Dica: Note que o número já está em formato string
    
    Exemplo:
      numero = 3667 -> True, pois o dígito 6 aparece consecutivo.
      numero = 1231 -> False, pois não possui dígito consecutivos.
    '''
    numero_chato = []
    for a in numero:
        a = int(a)
        numero_chato.append(a)
    if sum(numero_chato) % 2 != 0:
        return True
    else:
        return False


def encontra_caracter(texto, caracter):
    '''
    params texto: um texto em formato string
    params caracter: um caracter em formato string
    returns: retorna a posição que um caracter está em uma string.

    Deve procurar o caracter na string texto e informar a posição que o caracter aparece pela primeira vez. 

    Exemplo:
    encontra_caracter('Eduardo', 'a') -> 3
    encontra_caracter('Eduardo', '0') -> 6
    encontra_caracter('Eduardo', 'z') -> None

    Dica:
    Se o código não retornar nada, será considerado None
    '''
    for a, b in enumerate(texto):
        if b == caracter:
            return a


def encontra_menor_quantidade_de_chuva(chuvas_meses):
    '''
    params chuvas_meses: uma lista com a quantidade de chuva (em mm) de cada mês do ano
    returns: um valor int, correspondente ao menor volume de chuvas.

    Importante:
    Não podem ser usadas funções prontas da linguagem, com min() ou sort().

    Exemplo
    encontra_menor_quantidade_de_chuva([20, 10, 30, 6, 40]) -> deve retornar 6, pois esse é o menor volume de chuvas.
    '''
    menor_quantidade = chuvas_meses[1]
    for a, b in enumerate(chuvas_meses):
        if b < menor_quantidade:
            menor_quantidade = b
    return menor_quantidade


def encontra_mes_com_menos_chuva(chuvas_meses):
    '''
    params chuvas_meses: uma lista com a quantidade de chuva (em mm) de cada mês do ano
    returns: um valor string, correspondente ao mês com a menor quantidade de chuva.

    Descubra (sem utilizar funções prontas da linguagem) em
    qual mês caiu a menor quantidade de chuvas e devolva o
    nome desse mês. 

    Dica: crie uma lista com o nome dos meses e use a posição
    da lista com as chuvas para chegar no nome do mês desejado.

    Exemplo:
    encontra_mes_com_menos_chuva([20, 10, 6, 8, 15, 21, 12, 16, 18, 25, 30, 1]) -> 'mar'

    Os meses devem estar no formato 'jan', 'fev', 'mar', 'abr', ...
    '''
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    menor_mes = chuvas_meses[0]
    for a, b in enumerate(chuvas_meses):
        if b < menor_mes:
            menor_mes = b
            mes = meses[a]
    return mes

def quantidade_de_pares(valor_inicial,valor_final):
    '''
    params valor_inicial: um valor inteiro
    params valor_final: um valor inteiro
    returns: um valor inteiro, conforme regra a seguir

    Deve retornar a quantidade de números pares num intervalo.
    Importante:
        Inclua os valores inicial e final do intervalo.

    Exemplo:
    quantidade_de_pares(1, 6) -> 3 (pois entre 1 e 6, incluindo os extremos, encontramos os pares 2, 4, e 6)
    '''
    pares = []
    for k in range(valor_inicial, valor_final +1):
        if k % 2 == 0:
            pares.append(k)
    return len(pares)

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Falhou')
    else:
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print(' Troca caixa:')
    test(troca_caixa("Araquari"), "ArAqUArI")  # normal
    test(troca_caixa("Caxias do Sul"), "cAxIAs dO sUl")  # com espaços

    print(' Número legal:')
    test(numero_legal("8888"), True)
    test(numero_legal("8881"), False)

    print(' Número chato:')
    test(numero_chato("8823"), True)
    test(numero_chato("8231"), False)

    print(' Encontra caracter:')
    test(encontra_caracter("--*--", "*"), 2)
    test(encontra_caracter("19/05/2014", "9"), 1)
    test(encontra_caracter("19/05/2014", "."), None)

    print('Encontra menor quantidade de chuva:')
    test(encontra_menor_quantidade_de_chuva([10,20,15,9,12,25,23,14,21,20,16,17]), 9) 

    print('Encontra mês com menos chuva:')
    test(encontra_mes_com_menos_chuva([10,20,15,9,12,25,23,14,21,20,16,17]), 'abr') 
    test(encontra_mes_com_menos_chuva([30,20,15,19,12,25,23,14,21,20,16,7]), 'dez')

    print('Quantidade de pares:')
    test(quantidade_de_pares(2,3), 1)
    test(quantidade_de_pares(2,4), 2)
    test(quantidade_de_pares(1,10), 5)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (
        total, acertos, total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
