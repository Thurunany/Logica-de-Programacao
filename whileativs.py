def poupanca(saldo, quantidade_meses, juros_ao_mes):
    '''
    :param saldo: saldo inicial aplicado na poupanca. Valor 'float'
    :param quantidade_meses: quatidade de meses que o valor será aplicado.
        Valor 'int'
    :param juros_ao_mes: porcentual de juros mensal. Valor 'float'
    :returns: um novo saldo, com a correção dos meses de juros. Valor float.

    Tomar como base no saldo inicial de uma conta poupança, a quantidade de
    meses em que o dinheiro ficará aplicado e o juro mensal a ser aplicado.
    Calcular e retornar o saldo da poupança atualizado.

    Arredendar duas casas decimais
    '''
    
    contador = 0
    novo_saldo = saldo
    while contador < quantidade_meses:
        novo_saldo += novo_saldo * juros_ao_mes / 100
        contador += 1
    return novo_saldo

def pares_e_divisiveis_por_7(limite_inicial=1067, limite_final=3627):
    '''
    :param limite_inicial: número inicial. Valor padrão definido como 1067
    :param limite_final: número final. Valor padrão definido como 3627
    :returns: um inteiro com a quantidade números pares e divisíveis por 7.

    Entre 1067 e 3627 (inclusive), quantos números são pares e
    também divisíveis por 7?
    '''

    contador = limite_inicial
    numero_de_pares_e_divisiveis_por_sete = 0
    while contador <= limite_final:
        if contador % 2 == 0 and contador % 7 == 0:
            numero_de_pares_e_divisiveis_por_sete += 1
        contador += 1
    return numero_de_pares_e_divisiveis_por_sete







def divisivel_por_7_e_9(n=1):
    '''
    param n: valor inteiro. Se não for informado nenhum valor, assume-se 1
    return: um inteiro, representando o n-ésimo número divisível por 7 e 9

    Quais é o n-ésimo número divisível por 7 e 9?
    '''

    if n == 1:
        return 63 
    else:
        contador_de_n = 2
        while contador_de_n <= n:
        numero += 1
            if numero % 7 == 0 and numero % 9 == 0:
                contador_de_n += 1
            
    return numero


def intercalamento_contrario(lista1, lista2):
    '''
    param lista1: uma lista de números
    param lista2: uma lista de números
    returns: uma lista de números intercalando lista1 e lista2, conforme regra:

    Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    crie uma nova lista composta pelo intercalamento entre as duas.
    A primeira lista deve ser usada na ordem normal. Já a segunda, deve
    ser utilizada na ordem inversa.

    Exemplo:
        lista1 = [3, 9, 1, 4]
        lista2 = [8, 5, 6, 2]
        deve retornar a lista ==> [3, 2, 9, 6, 1, 5, 4, 8]
    '''


    lista2.reverse()
    contador = 0
    nova_lista = []
    while contador < len(lista1):
        nova_lista.append(lista1[contador])
        nova_lista.append(lista2[contador])
        contador += 1
    return nova_lista



def maiores_13(idades, alturas):
    '''
    param idades: uma lista com as idades de pessoas
    param alturas: uma lista com as alturas de pessoas
    returns: uma lista com alturas conforme a regra a seguir:

    A função recebe as idades e alturas de diversas pessoas, em duas
    listas separadas e de igual comprimento.
    Calcule a media das alturas e retorne as alturas daqueles que possuem
    'idades' maior que 13 e altura inferior a media de altura da turma'''

    media_das_alturas = sum(alturas) / len(alturas)
    contador = 0
    nova_lista = []
    while contador < len(idades):
        if idades[contador] > 13 and alturas[contador] < media_das_alturas:
            nova_lista.append(alturas[contador])
        contador += 1
    return nova_lista





#  Área de testes: só mexa aqui se souber o que está fazendo!
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
    print('Poupança:')
    test(poupanca(1000, 1, 1), 1010.00)
    test(poupanca(1000, 2, 1), 1020.10)
    test(poupanca(1000, 1, 2), 1020.00)
    test(poupanca(1000, 2, 2), 1040.40)

    print('Pares e divisíveis por 7:')
    test(pares_e_divisiveis_por_7(), 183)

    print('Pares e divisíveis por 7:')
    test(divisivel_por_7_e_9(), 63)
    test(divisivel_por_7_e_9(2), 126)
    test(divisivel_por_7_e_9(3), 189)

    print(' Lista intercalada contrária:')
    test(intercalamento_contrario([], []), [])
    test(intercalamento_contrario([1], [2]), [1, 2])
    test(intercalamento_contrario([1, 2], [3, 4]), [1, 4, 2, 3])
    test(intercalamento_contrario([1, 2, 3], [4, 5, 6]), [1, 6, 2, 5, 3, 4])
    test(intercalamento_contrario([1, 2, 3, 4, 5], [
         6, 7, 8, 9, 10]), [1, 10, 2, 9, 3, 8, 4, 7, 5, 6])

    print(' Alturas abaixo da media:')
    test(maiores_13([13, 13, 14], [1.7, 1.7, 1.5]), [1.5])
    test(maiores_13([13, 13, 14, 13], [1.7, 1.7, 1.5, 1.6]), [1.5])
    test(maiores_13([14, 20], [1.6, 2]), [1.6])
    test(maiores_13([10, 7, 13, 15, 20, 21], [
         1.7, 1.21, 1.65, 2, 1.9, 1.5]), [1.5])
    test(maiores_13([14, 15, 16, 17, 18, 30], [
         1.9, 1.89, 1.85, 1.95, 2, 1.99]), [1.9, 1.89, 1.85])
    test(maiores_13([10, 9, 90, 9, 13, 14, 15], [
         1.25, 1.3, 1.7, 1.41, 1.5, 1.55, 1.7]), [])


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (
        total, acertos, total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
