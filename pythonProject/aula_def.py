import random
def menu():
    print('\t-----Escolha a questão-----'
          '\n\t|1-Dobrando os valores da lista|'
          '\n\t|2-Calcule a área do terreno   |'''
          '\n\t|3-Seno Cosseno Tangente       |'
          '\n\t|4-Sorteia um nome             |'
          '\n\t|5-Sorteia a ordem dos alunos  |'
          '\n\t|0-Encerrar programa           |')


def soma(*valores):
    ss = 0
    for numm in valores:
        ss += numm
    print(f'Somando os valores {valores} = {ss} ')
    
def sorteio(sorte):
    ordem_sorteio = random.sample(sorte, len(sorte))
    return ordem_sorteio


# desempacotamento

def atualiza_dic(**valores):
    for k in valores:
        if valores["nome"] == k["nome"]:
            k.update(valores)
    for X, Y in valores.items():
        print(f'{X}: {Y}')


def dic(**pessoa):
    for X, y in pessoa.items():
        print(f'{X}: {y}')


def contador(*num1):  # neste caso é criado uma tupla
    print(num1)
    tam = len(num1)
    for valor in num1:
        print(f'{valor}->', end='')
    print('FIM')
    ss = sum(num1)
    print(ss)
    print(f'\nvalores recebidos {num1} e sao ao todo {tam}')


def dobra(lst):
    aux = 0
    while aux != len(lst):
        lst[aux] *= 2
        aux += 1
    for valor in lst:
        print(f'{valor}-> ', end='')
    print('FIM')


def area(a, b):
    ar = a * b
    print('A área do seu terreno é {}'.format(ar))


aux1 = -1
contador(1, 3, 4, 10, 20, 25)
while aux1 != 0:

    menu()
    aux2 = int(input("Qual questão deseja?"))

    if aux2 == 0:
        print('Atividade encerrada, volte sempre!\n')
        aux1 = 0
        pass

    elif aux2 == 1:
        lista = list()
        for v in range(0, 5):
            v = float(input('Informe um valor!'))
            lista.append(v)

        dobra(lista)
        pass

    elif aux2 == 2:
        print('-' * 10, 'INFORME AS DIMENSÕES DO SEU TERRENO', '-' * 10)
        base = float(input('informe o comprimento '))
        altura = float(input('informe a altura do terreno '))
        area(base, altura)
        pass

    elif aux2 == 3:
        num = int(input('informe quantos cadastros deseja fazer !'))
        lista = list()
        cadastro = dict()

        for x in range(0, num):
            cadastro['nome'] = str(input('Informe o seu nome !'))
            cadastro['idade'] = int(input('informe a sua idade'))
            lista.append(cadastro.copy())

        nome_al = str(input('Informe um nome !'))
        atualiza_dic(lista, nome=nome_al)
        pass
        
    elif aux2 == 4:
        alunos = ["kalliny", "Marcony", "Fabrício", "Cainan"]
        revistas = ["inderscience", "ijcnis", "wordcientific", "ciencedirect"]
        
        ordem_sorteada = sorteio(alunos)

        print("Ordem sorteada dos alunos:")
        for i,rev in enumerate(revistas, start=1):
            print(f"{i}. {rev}")
        print("-"*30)
        for i, aluno in enumerate(ordem_sorteada, start=1):
            print(f"{i}. {aluno}")