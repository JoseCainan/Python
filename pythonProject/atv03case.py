def pesquisar(aux, lista):
    for cadastro in lista:
        for _, _ in cadastro.items():
            if cadastro['cpf'] == aux:
                '''for x, v in cadastro.items():
                    print(f'{x} = {v}')'''
                return aux
    print("funcionário nao encontrado")


def up_telefone(aux, lista):
    for dicionário_aux in lista:
        for _, _ in dicionário_aux.items():
            if dicionário_aux['nome'] == aux:
                print('-' * 30, 'Atualize o telefone do funcionário', '-' * 30)
                dicionário_aux['fone'] = str(input('Informe o seu telefone'))
                return


def up_dados(aux, lista, lista_t):
    for dicionário_aux in lista:
        if dicionário_aux['nome'] == aux:
            lista.remove(dicionário_aux)
            print('-' * 30, 'Atualize os dados do funcionário', '-' * 3)
            dicionário_aux['cpf'] = str(input('Informe seu CPF: '))
            dicionário_aux['nome'] = str(input('Informe o seu nome: '))
            dicionário_aux['cargo'] = str(input('Informe o seu cargo: '))
            dicionário_aux['salario'] = float(input('Informe o salario do funcionário: '))
            lista.append(dicionário_aux)
            break

    for dicionário_aux in lista_t:
        for _, _ in dicionário_aux.items():
            if dicionário_aux['nome'] == aux:
                print('-' * 30, 'Atualize o telefone do funcionário', '-' * 30)
                dicionário_aux['nome'] = str(input('informe o nome novamente'))
                dicionário_aux['fone'] = str(input('Informe o telefone'))


def delete_func(auxiliar, lista, lista_tel):
    for deletar in lista:
        if deletar['nome'] == auxiliar:
            lista.remove(deletar)

    for deletar_tel in lista_tel:
        if deletar_tel['nome'] == auxiliar:
            lista_tel.remove(deletar_tel)


nub = -1
num = int(input('informe quantos cadastros deseja fazer !'))
Lista = list()
cadastro = dict()
lis_tel = list()

for x in range(0, num):
    cadastro['cpf'] = str(input('Informe o CPF do funcionário!'))
    cadastro['nome'] = str(input('Informe o nome do funcionário !'))
    cadastro['cargo'] = str(input('informe o cargo do funcionário'))
    cadastro['fone'] = str(input('Informe o telefone do funcionário'))
    cadastro['salario'] = float(input('Informe o salario do funcionário'))
    Lista.append(cadastro.copy())

for new in Lista:
    new_dict = {"nome": new["nome"], "fone": new["fone"]}
    lis_tel.append(new_dict)

for delete in Lista:
    del delete['fone']

print('-' * 30, 'lista de funcionários', '-' * 30)

for aux in Lista:
    print('-' * 30)
    for x, v in aux.items():
        print(f'{x} = {v}')

print('-' * 30, 'lista de Telefones', '-' * 30)

for aux in lis_tel:
    print('-' * 30)
    for x, v in aux.items():
        print(f'{x} = {v}')

while nub != 0:
    print('\t-----Escolha a questão-----'
          '\n\t|   1-Buscar CPf                              |'
          '\n\t|   2-Editar telefone                         |'
          '\n\t|   3-Editar dados do funcionário             |'
          '\n\t|   4-Imprimir listas                         |'
          '\n\t|   5-Demitir Funcionário                     |'
          '\n\t|   6-Ad3icionar Funcionário                   |'
          '\n\t|0-Digite zero para encerrar a lista de questões|\n')

    op = int(input("Qual questão deseja?"))

    if op < 0 or op > 6:
        print("Questão inexistente !")
        # break
    elif op == 0:
        print('Programa encerrado !')
        nub = 0

    elif op == 1:
        aux = input('Qual cpf deseja buscar ?\n')
        pesquisar(aux, Lista)

    elif op == 2:
        aux = input('informe o nome do funcionário para editar o telefone !')
        up_telefone(aux, lis_tel)

    elif op == 3:
        aux = input('informe o nome do funcionário para editar os dados !')
        up_dados(aux, Lista, lis_tel)

    elif op == 4:
        print('-' * 30, 'lista de funcionários', '-' * 30)
        for aux in Lista:
            print('-' * 30)
            for x, v in aux.items():
                print(f'{x} = {v}')

        print('-' * 30, 'lista de Telefones', '-' * 30)
        for aux in lis_tel:
            print('-' * 30)
            for x, v in aux.items():
                print(f'{x} = {v}')

    elif op == 5:
        print('-' * 30, 'Demissão de Funcionário', '-' * 30)
        aux = input('informe o nome do funcionário que deseja demitir')
        delete_func(aux, Lista, lis_tel)
        print("Funcionário {} demitido".format(aux))

    elif op == 6:
        cadastro['cpf'] = str(input('Informe seu CPF !'))
        nome = cadastro['nome'] = str(input('Informe o nome do funcionário !'))
        cadastro['cargo'] = str(input('informe o cargo do funcionário'))
        cadastro['salario'] = float(input('Informe o salario do funcionário'))
        Lista.append(cadastro.copy())

        novo_tel = {"nome": nome, "fone": str(input('informe o novo telefone'))}
        lis_tel.append(novo_tel)

        chave = 'fone'
        for funcionário in Lista:
            if chave in funcionário:
                del funcionário[chave]
