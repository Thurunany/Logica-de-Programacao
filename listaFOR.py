# Lista de exercícios 3 - Estruturas de repetição For
# Utilizar for sempre que possível
# Utilizar "for item in lista" sempre que possível
# Utilizar "for i, item in enumerate(lista)" sempre que possível


def soma(lista):
    """Retorna a soma dos elementos de uma lista"""
    soma = 0
    for num in lista:
        soma += num


def quantidade_de_impares(valor_inicial, valor_final):
    """ Determine a quantidade de números ímpares num intervalo"""
     
    contador_de_impares = 0
    for numero in range(valor_inicial + 1, valor_final):
        if numero % 2 == 1:
            contador_de_impares += 1
    return contador_de_impares     

def soma_dos_inteiros(valor1, valor2):
    """ Calcule a soma dos números inteiros no intervalo entre 'valor1'
    e o 'valor2' ou vice-versa, considerando que podem ser informado
    números negativos ou fora de ordem.
    Ex: 1 e 5 ou 5 e 1, retorna 9"""

    soma = 0 
    if valor1 < valor2:
        for numero in range(valor1 + 1, valor2):
            soma += numero
    else:
        for numero in range(valor2 + 1, valor1):
            soma += numero
    return soma 

def serie(fim):
    """Dado n, calcule o valor de
    s = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n """
    s = 0 
    for numero in range(1, fim + 1):
        s+= 1/ numero
    return round (s, 2)

def ordenamento_contrario(lista):
    """ Inverta a lista """
    nova_lista = []
    for elemento in lista[::-1]:
        nova_lista.append(elemento)
    return nova_lista

def intercalamento_listas(lista1, lista2):
    """ Usando 'lista1' e 'lista2', ambas do mesmo comprimento,
    crie uma nova lista composta pelo intercalamento entre as duas."""

    nova_lista = []
    for i in range(len(lista1)):
        nova_lista.append(lista1[i])
        nova_lista.append(lista2[i])
    return nova_lista

def im_pares(lista):
    """ Separe em listas os impares e pares, dos inteiros da 'lista' """

    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares


def maior_menor(lista):
    """ Calcule o maior e o menor numero da 'lista' """

    menor = lista[0]
    maior = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
    return maior, menor

def dar_troco(valor_a_pagar, valor_em_dinheiro):
    """ Calcule o troco numa lista com notas de 1,2,5,10,20,50 com sua
    quantidade de notas sem considerar centavos

    ex:
    1 e 10 retorna troco_notas_quantidade = [5,2] quantidade_notas = [1,2]"""

    notas = (50, 20, 10, 5, 2, 1)
    valor_troco = valor_em_dinheiro - valor_a_pagar
    troco = []
    for nota in notas:
        quantidade = valor_troco // nota
        valor_troco= valor_troco % nota
        if quantidade != 0:
            troco.append((nota, quantidade))
    return troco



def media_anual(temperaturas):
    """Receba uma lista com as temperaturas médias de cada mês
    e devolva uma lista com os números correspondentes aos meses
    que possuem temperatura superior á média anual."""

    media = sum(temperaturas) / len(temperaturas)
    meses_acima_da_media = []
    for mes, temperatura in enumerate(temperaturas):
        if temperatura > media:
            meses_acima_da_media.append(mes)
    return meses_acima_da_media

def maiores_13(idades, alturas):
    """Esta função recebe as idades e alturas de diversas pessoas, em duas
    listas separadas e de igual comprimento.
    Calcule a media das alturas e retorne as alturas daqueles que
    possuem 'idades' maior que 13 e altura inferior a media da turma"""

    media_das_alturas = sum(alturas) / len(alturas)
    alturas_abaixo_media_maiores_13 = []
    for i in range(len(idades)):
        if idades[i] > 13 and alturas[i] < media_das_alturas:
            alturas_abaixo_media_maiores_13.append(alturas[i])
    return alturas_abaixo_media_maiores_13


def testa_primo(valor):
    """Recebe um valor e verifica se ele é um número primo ou não."""

    if valor == 2:
        return True
    if valor in (0,1) or valor % 2 == 0:
        return False
    for i in range(2, valor):
        if valor % i == 0:
            return False
    return True

def lista_de_primos(inicio, fim):
    """Retorne uma lista de primos entre os valores informados, incluindo
    os limites"""

    lista_primos = []
    for numero in range(inicio, fim + 1):
        if testa_primo(numero):
            lista_primos.append(numero)
    return lista_primos

def Fibonacci(n):
    """ Retorne uma lista com os n primeiros valores da série de Fibonacci.
    Fibonacci = 1,1,2,3,5,8,13,..."""
    ant_1 = 1
    ant_2 = 0
    fib = []
    for i in range(n):
        soma = ant_1 + ant_2
        ant_1 = ant_2
        ant_2 = soma
        fib.append(soma)
    return fib


def altera_salarios(salarios):
    """ Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5%
    Salário mínimo para referência: R$ 724,00
    Retorna a lista com os salários alterados
    """
    salario_minimo = 724
    novos_salarios = []
    for salario in salarios:
        if salario <= salario_minimo:
            novo_salario = salario * 1.2
        elif salario <= 2 * salario_minimo:
            novo_salario = salario * 1.15
        elif salario <= 5 * salario_minimo:
            novo_salario = salario * 1.1
        else:
            novo_salario = salario * 1.05
        novos_salarios.append(round(novo_salario, 2))
    return novos_salarios


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
    print('Quantidade de ímpares:')
    test(quantidade_de_impares(1, 50), 24)
    test(quantidade_de_impares(1, 10), 4)
    test(quantidade_de_impares(1, 60), 29)
    test(quantidade_de_impares(40, 80), 20)

    print('Soma de números inteiros:')
    test(soma_dos_inteiros(1, 5), 9)
    test(soma_dos_inteiros(1, 50), 1224)
    test(soma_dos_inteiros(50, 1), 1224)
    test(soma_dos_inteiros(10, 1), 44)
    test(soma_dos_inteiros(-10, 1), -45)
    test(soma_dos_inteiros(10, -10), 0)

    print('Série:')
    test(serie(1), 1.00)
    test(serie(15), 3.32)
    test(serie(10), 2.93)
    test(serie(5), 2.28)

    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [-1, 0]
    lista3 = [-10, 0, 10, 2, 100, -100, -100.1]
    lista4 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    lista5 = [1, 3, 5, 7, 9]
    lista6 = [2, 4, 6, 8, 10]

    print(' Listas invertidas:')
    test(ordenamento_contrario(lista1), ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    test(ordenamento_contrario(lista2), ([0, -1]))
    test(ordenamento_contrario(lista3), ([-100.1, -100, 100, 2, 10, 0, -10]))

    print(' Lista Intercalada:')
    test(intercalamento_listas(lista5, lista6),
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(' Lista de pares e impares:')
    test(im_pares(lista1), ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9]))
    test(im_pares(lista5), ([], [1, 3, 5, 7, 9]))
    test(im_pares(lista6), ([2, 4, 6, 8, 10], []))

    print(' Maior e o menor da lista:')
    test(maior_menor(lista1), (10, 1))
    test(maior_menor(lista2), (0, -1))
    test(maior_menor(lista3), (100, -100.1))
    test(maior_menor(lista4), (-1, -10))

    print(' Troco do pagamento:')
    test(dar_troco(10, 10), [])
    test(dar_troco(1, 201), [(50, 4)])
    test(dar_troco(10, 148), [(50, 2), (20, 1),
                              (10, 1), (5, 1), (2, 1), (1, 1)])
    test(dar_troco(10, 109), [(50, 1), (20, 2), (5, 1), (2, 2)])

    print(' Meses acima da média:')
    test(media_anual([20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]), [])
    test(media_anual([25, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]), [0])
    test(media_anual([23, 25, 26, 24, 21, 22, 26,
                      24, 25, 22, 23, 19]), [1, 2, 3, 6, 7, 8])
    test(media_anual([19, 20, 21, 20, 17, 18, 19, 20, 22, 21, 20]), [
         1, 2, 3, 7, 8, 9, 10])
    test(media_anual([21, 22, 23, 21, 22, 22, 23, 21, 23, 22, 21, 23, 21]), [
         1, 2, 4, 5, 6, 8, 9, 11])

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

    print(' Lista de primos:')
    test(lista_de_primos(0, 1), [])
    test(lista_de_primos(5, 10), [5, 7])
    test(lista_de_primos(10, 20), [11, 13, 17, 19])
    test(lista_de_primos(0, 21), [2, 3, 5, 7, 11, 13, 17, 19])
    test(lista_de_primos(43, 102), [43, 47, 53,
                                    59, 61, 67, 71, 73, 79, 83, 89, 97, 101])

    print(' Fibonacci:')
    test(Fibonacci(1), [1])
    test(Fibonacci(2), [1, 1])
    test(Fibonacci(3), [1, 1, 2])
    test(Fibonacci(4), [1, 1, 2, 3])

    print(' Aumenta salários:')
    test(altera_salarios([
        500, 724.0, 725.00, 1448.00, 1449.00, 3620.00, 3621.00, 4000.00]),
        [600.0, 868.8, 833.75, 1665.2, 1593.9, 3982.0, 3802.05, 4200.0])


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (
        total, acertos, total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
