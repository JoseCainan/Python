def menu():
    print('\t-----Escolha a questão-----'
          '\n\t|1-Dobrando os valores da lista|'
          '\n\t|2-Calcule a área do terreno   |'''
          '\n\t|3-Seno Cosseno Tangente       |'
          '\n\t|4-Sorteia um nome             |'
          '\n\t|5-Sorteia a ordem dos alunos  |'
          '\n\t|0-Encerrar programa           |')


def area(a, b):
    ar = a * b
    print('A área do seu terreno é {}'.format(ar))


def atualiza_dic(valores):
    for k in valores:
        if valores["nome"] == k["nome"]:
            k.update(valores)
    for X, Y in valores.items():
        print(f'{X}: {Y}')


aux1 = -1
while aux1 != 0:

    menu()
    aux2 = int(input("Qual questão deseja?"))

    if aux2 == 0:
        print('Atividade encerrada, volte sempre!\n')
        aux1 = 0

    elif aux2 == 1:
        lista = list()
        for v in range(0, 5):
            v = float(input('Informe um valor!'))
            lista.append(v)

        dobra(lista)

    elif aux2 == 2:
        print('-' * 10, 'INFORME AS DIMENSÕES DO SEU TERRENO', '-' * 10)
        base = float(input('informe o comprimento '))
        altura = float(input('informe a altura do terreno '))
        area(base, altura)

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


