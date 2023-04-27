nub = -1
while nub != 0:
    print('\t-----Escolha a questão-----'
          '\n\t|   1-Cadastro de pessoas                     |'
          '\n\t|   2-Dicionários maiores e menores de 18 anos|'
          '\n\t|   3-Dicinário backup                        |'
          '\n\t|0-Digite zero para encerrar a lista de questões|\n')

    op = int(input("Qual questão deseja?"))

    if op < 0 or op > 6:
        print("Questão inexistente !")
        # break
    elif op == 0:
        print('Programa encerrado !')

    elif op == 1:
        num = int(input('informe quantos cadastros deseja fazer !'))
        lista = list()
        cadastro = dict()

        for x in range(0, num):
            cadastro['cpf'] = str(input('Informe seu CPF !'))
            cadastro['nome'] = str(input('Informe o seu nome !'))
            cadastro['idade'] = int(input('informe a sua idade'))
            cadastro['fone'] = str(input('Informe o seu telefone'))
            lista.append(cadastro.copy())

        # for nome in lista:
        #  print(nome)
        for aux in lista:
            print('-' * 30)
            for x, v in aux.items():
                print(f'{x} = {v}')

        # break

    elif op == 2:
        num = int(input('informe quantos cadastros deseja fazer !'))
        lista2 = list()
        cadastro2 = dict()
        lista3 = list()
        dicc = dict()

        for x in range(0, num):
            cadastro2['cpf'] = str(input('Informe seu CPF !'))
            cadastro2['nome'] = str(input('Informe o seu nome !'))
            cadastro2['idade'] = int(input('informe a sua idade'))
            lista2.append(cadastro2.copy())

        for dicionario in lista2:
            if dicionario['idade'] < 18:
                dicc.update(dicionario)
                lista3.append(dicc.copy())

        print('-' * 10, 'dicionários originais', '-' * 10)
        for e in lista2:
            for aux1, aux2 in e.items():
                print(f'{aux1} = {aux2}')
        print('-' * 10, 'dicionários menor de idade', '-' * 10)
        for e in lista3:
            for aux3, aux4 in e.items():
                print(f'{aux3} == {aux4}')


    elif op == 3:
        dicionario_back = dict()
        aux = 0
        op2 = -1

        while op2 <= 0:
            dicionário_or = dict()
            while aux < 5:
                la1 = input('informe a chave do dicionário nao obs: repita as chaves !')
                dicionário_or[la1] = input('informe o contudo')
                aux += 1
            dicionario_back.update(dicionário_or)

            for aux1, aux2 in dicionário_or.items():
                print(f'{aux1} = {aux2}')

            del dicionário_or

            print('-' * 10, 'dicionário backup', '-' * 10)

            for aux1, aux2 in dicionario_back.items():
                print(f'{aux1} = {aux2}')

            aux = 0
            print('digite 1 para encerrar e 0 para continuar !')
            op2 = int(input('deseja encerrar a questão?'))

        # break
    print('digite 0 para encerrar e 1 para continuar !')
    nub = int(input('deseja acabar o programa ?'))
