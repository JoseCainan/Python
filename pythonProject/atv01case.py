def menu():
    print('\t-----Escolha a questão-----'
          '\n\t|1-Números inteiros na lista|'
          '\n\t|2-Lista na ordem inversa   |'''
          '\n\t|3-Média de notas           |'
          '\n\t|4-Vogais e consoantes      |'
          '\n\t|5-Números pares e impares  |'
          '\n\t|6-Média de dez alunos      | '
          '\n\t|0-Encerrar programa        |')


op = -1
while op != 0:

    menu()

    op = int(input("Qual questão deseja?"))

    if op < 0 or op > 6:
        print("Questão inexistente !")
        # break
    elif op == 0:
        print('Programa encerrado !')

    elif op == 1:
        nova_list = []
        for element in range(0, 5):
            item = int(input('informe um elemento'))
            nova_list.append(item)

        print(nova_list)
        # break

    elif op == 2:
        Lista = []
        for element in range(0, 10):
            item = int(input('informe um elemento'))
            Lista.append(item)

        print(Lista)
        Lista.reverse()
        print(Lista)
        # break

    elif op == 3:
        Lista_nova = []
        for element in range(0, 4):
            item = int(input('informe uma nota'))
            Lista_nova.append(item)

        media = sum(Lista_nova) / 4
        print(media)
        # break

    elif op == 4:
        lista = []
        vogal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        conso = []
        for element in range(0, 10):
            item = input('informe um caracter')
            lista.append(item)
        for caracter in lista:
            if caracter not in vogal:
                conso.append(caracter)

        print(lista)
        print(conso)
        print('a lista possui {}, consoantes'.format(len(conso)))
        # break

    elif op == 5:
        lista_or = []
        lista_impar = []
        lista_par = []

        for element in range(0, 20):
            item = int(input('informe um número'))
            lista_or.append(item)

        lista_par = [item for item in lista_or if item % 2 == 0]
        lista_impar = [item for item in lista_or if item % 2 != 0]

        print('lista original', lista_or)
        print('lista par', lista_par)
        print('lista impar', lista_impar)
        # break

    elif op == 6:
        '''nova_list = []
        medias_list = []
        media = 0
        aux = 0
        while aux < 5:
             for item in range (0, 4):
                  item = int(input('informe uma nota'))
                  nova_list.append(item)
                  aux +=1
             media = sum(nova_list) / 4
             medias_list.append(media)

        print(medias_list)'''
        nova_list = []
        medias_list = []
        media = 0

        for item in range(0, 10):
            n1 = float(input('informe a nota 1'))
            n2 = float(input('informe a nota 2'))
            n3 = float(input('informe a nota 3'))
            n4 = float(input('informe a nota 4'))
            media = (n1 + n2 + n3 + n4) / 4
            medias_list.append(media)

        print(medias_list)

        for pos, nota in enumerate(medias_list):
            if nota >= 7:
                print('aluno {}: {}'.format(pos, nota))

        # break
