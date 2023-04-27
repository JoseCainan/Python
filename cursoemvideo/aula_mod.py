# trabalhando com módulos
""" Biblioteca math
ceil = função que arredonda para cima
floor = função que arredonda para baixo
sqrt = raiz quadrada
factorial ?
import math = importa tudo
from math import sqrt = nesse caso só é importado a função sqrt e
voce pode usar so sqrt sem a necessidade de colocar math.sqrt
"""
import math
import random


def menu():
    print('\t-----Escolha a questão-----'
          '\n\t|1-Parte inteira do número    |'
          '\n\t|2-Hipotenusa                  |'''
          '\n\t|3-Seno Cosseno Tangente       |'
          '\n\t|4-Sorteia um nome             |'
          '\n\t|5-Sorteia a ordem dos alunos  |'
          '\n\t|0-Encerrar programa           |')


aux1 = -1

while aux1 != 0:

    menu()
    aux2 = int(input("Qual questão deseja?"))

    if aux2 == 0:
        print('Atividade encerrada, volte sempre!\n')
        aux1 = 0

    elif aux2 == 1:
        """num = float(input('informe um número'))
        num = num // 1
        print(num)"""
        num = float(input('informe um número !'))
        num = math.trunc(num)
        print('A parte inteira é: {}'.format(num))
        num = 0

    elif aux2 == 2:
        cateto_op = float(input('Informe o cateto oposto'))
        cateto_ad = float(input('informe o cateto adjacente '))

        hipotenusa = math.sqrt((cateto_ad * cateto_ad) + (cateto_op * cateto_op))
        print(f'Cateto oposto: {cateto_op}\nCateto adjacente: {cateto_ad}\nHipotenusa: {hipotenusa}')

    elif aux2 == 3:
        número = float(input('Informe um ângulo em graus'))
        seno = math.sin(número)
        cosseno = math.cos(número)
        tangente = math.tan(número)

        print('Cosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}\n'.format(cosseno, seno, tangente))

    elif aux2 == 4:
        lista = list()
        for item in range(0, 4):
            item = input('Informe um nome!')
            lista.append(item)

        sorteio = random.choice(lista)
        print(sorteio)

    elif aux2 == 5:
        lista = list()
        for it in range(0, 4):
            it = input('Informe um nome!')
            lista.append(it)
        num = 0
        for it in range(0, 4):
            it = random.choice(lista)
            num += 1
            print(f'aluno {num}: {it}')
            lista.remove(it)
