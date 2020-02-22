# Lista de exercícios 3


def testa_lados(a,b,c):
    ''' Receba os três lados de um triângulo. Informe se os valores 
    podem ser um triângulo. Indique, caso os lados formem um triângulo, 
    se o mesmo é: equilátero, isósceles ou escaleno. '''

    if (b + c) < a or (a + c) < b or (a + b) < c:
        return "Não forma um triângulo"
    elif (a == b) and (b == c):
        return "Triângulo equilátero"
    elif (a == b) or (b == c) or (a == c):
        return "Triângulo isósceles"
    else:
        return "Triângulo escaleno"

 
def ano_bissexto(ano):
    ''' Determine se um ano é bissexto'''

    if ano % 4 == 0 and ano % 100 != 0: 
        return True

    elif ano % 400 == 0:
        return True

    return False 

def data_valida(data):
    '''Valida data. Recebe uma string no formato dd/mm/aaaa e informa
    um valor lógico indicando se a data é válida ou não.'''

    data = data.split('/')
    dia = data[0]
    mes = data[1]
    ano = data[2]
    
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

     
    if dia < 1:
        return False  

    elif mes < 1 or mes >= 13:
        return False

    elif ano == 0:
        return False 

    elif mes in (1, 3, 5, 7, 8, 10, 12) and dia <= 31:
        return True

    elif mes in (4, 6, 9, 11) and dia <= 30:
        return True 

    elif ano % 4 == 0 and ano % 100 != 0: 
        return True

    elif ano % 400 == 0 and dia <= 29:
        return True

    return False




def maior3(a,b,c):
    ''' Recebe tres valores, e retorna o maior dos tres'''

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b

    return c
     

def menor3(a,b,c):
    ''' Recebe tres valores, e retorna o menor dos tres'''

    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b

    return c

def baskara(a,b,c):
    '''Calcule as raízes de uma equação do segundo grau, na forma 
    ax2 + bx + c. A função recebe a, b e c e faz as consistências, 
    informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero é uma equaçao do 
    1o grau.
    - Se o delta calculado for negativo, a equação não possui raizes reais. 
    Devolva uma tupla vazia.
    - Se o delta calculado for igual a zero a equação possui apenas uma 
    raiz real. Devolva uma tupla com um único valor.
    - Se o delta for positivo, a equação possui duas raiz reais.
    Devolva uma tupla com dois elementos.
    '''
    
    if a == 0:
        return(-c/b, ) 

    else:

        delta = (b**2)-(4*a*c)
        x1=(-b + (delta ** 0.5)) / (2 * a)  
        x2=(-b - (delta ** 0.5)) / (2 * a)

        if delta < 0:
            return ( )
        elif delta ==  0:
            return (x1, )
    
    return (x1,x2)

'''

    delta = (b ** 2) - (4 * a * c) 

    x = (-b + (delta ** 0.5)) / (2 * a)
    y = (-b - (delta ** 0.5)) / (2 * a)

    raizes = (x, y, )

    if delta < 0:
        return ( )

    elif delta == 0:
        return (x, )

    elif a == 0:
        return (-b/c,) 

    return raizes

'''

def acrescimo_nota_bb(nota_sozinho,nota_com_ajuda):
    ''' Recebe a nota do litle brother antes de receber ajuda, e a nota
    depois que o big brother ajudou, e retorna o acrecimo que o big
     brother recebera em sua nota pela ajuda.
     O acréscimo é de 1/4 da diferença das notas, se for positivo'''











# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' %('Falhou')
    else:
        prefixo = '\033[32m%s' %('Passou')
        acertos += 1
    print ('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado), 
        repr(obtido)))

def main():
    print('Triângulos:')
    test(testa_lados(7,1,2),'Não forma um triângulo')
    test(testa_lados(7,2,1),'Não forma um triângulo')
    test(testa_lados(1,7,2),'Não forma um triângulo')
    test(testa_lados(1,2,7),'Não forma um triângulo')
    test(testa_lados(2,1,7),'Não forma um triângulo')
    test(testa_lados(2,7,1),'Não forma um triângulo')
    test(testa_lados(2,2,2),'Triângulo equilátero')
    test(testa_lados(3,3,3),'Triângulo equilátero')
    test(testa_lados(2,3,4),'Triângulo escaleno')
    test(testa_lados(2,4,3),'Triângulo escaleno')
    test(testa_lados(3,4,2),'Triângulo escaleno')
    test(testa_lados(3,2,4),'Triângulo escaleno')
    test(testa_lados(2,3,3),'Triângulo isósceles')
    test(testa_lados(3,2,2),'Triângulo isósceles')
    test(testa_lados(3,3,2),'Triângulo isósceles')
    test(testa_lados(3,2,3),'Triângulo isósceles')

    print('Ano bissexto:')
    test(ano_bissexto(1000),False)
    test(ano_bissexto(1200),True)
    test(ano_bissexto(1004),True)
    test(ano_bissexto(1040),True)
    test(ano_bissexto(2012),True)
    test(ano_bissexto(2014),False)

    print('Valida datas:')
    test(data_valida("01/01/2014"),True)
    test(data_valida("31/01/2014"),True)
    test(data_valida("00/00/0000"),False)
    test(data_valida("30/04/2014"),True)
    test(data_valida("31/04/2014"),False)
    test(data_valida("30/09/2014"),True)
    test(data_valida("31/09/2014"),False)
    test(data_valida("30/06/2014"),True)
    test(data_valida("31/06/2014"),False)
    test(data_valida("30/11/2014"),True)
    test(data_valida("31/11/2014"),False)
    test(data_valida("32/01/2014"),False)
    test(data_valida("01/01/0000"),False)
    test(data_valida("01/13/2014"),False)
    test(data_valida("01/00/2014"),False)
    test(data_valida("29/02/2014"),False)
    test(data_valida("29/02/2016"),True)

    print('Maior de 3 valores:')
    test(maior3(1,2,3), 3)
    test(maior3(1.01,1.1,1.02), 1.1)
    test(maior3(0,-1,-2), 0)
    test(maior3(-100,0,100), 100)

    print('Menor de 3 valores:')
    test(menor3(1,2,3), 1)
    test(menor3(1.01,1.02,1.1), 1.01)
    test(menor3(0,-1,-2), -2)
    test(menor3(-100,0,100), -100)

    print('Báskara:')
    test(baskara(1,4,4), (-2.0,))
    test(baskara(1,5,4), (-1.0, -4.0))
    test(baskara(0,4,2), (-0.5,))
    test(baskara(4,4,4), ())

    print('Acréscimo BB:')
    test(acrescimo_nota_bb(1,10), 2.2)
    test(acrescimo_nota_bb(7,6), 0.0)
    test(acrescimo_nota_bb(0,10), 2.5)
    test(acrescimo_nota_bb(6.9,7.1), 0.0)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
