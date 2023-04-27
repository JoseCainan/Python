def menu():
    print('-' * 20, 'MENU', '-' * 20)
    print('|0-sair do programa           |\n'
          '|1-Gerenciamento de Motoristas|\n'
          '|2-Gerenciamento de Veiculos  |\n'
          '|3-Gerenciamento de Viagem    |\n '
          '|4-Abastecimento da frota     |\n'
          '|5-Manutenção dos veiculos    |\n')


def menu_abastecimento():
    print('Opções o gerenciamento de abastecimento\n')
    print('\t4.0- voltar para o gerenciamento\n'
          '\t4.1- Cadastrar novo abastecimento\n'
          '\t4.2- Imprimir abastecimentos\n')


def menu_manutenção():
    print('\t5.0- voltar ao gerenciamento\n'
          '\t5.1- Cadastrar nova manutenção\n'
          '\t5.2- Imprimir manutenção\n')


def menu_motora():
    print('Opções o gerenciamento de motoristas\n')
    print('\t1.0- volte para o menu de gerenciameto\n'
          '\t1.1- Cadastrar novo motorista\n'
          '\t1.2- Pesquisar Motorista\n'
          '\t1.3- Editar motorista\n'
          '\t1.4- Deletar Motorista\n'
          '\t1.5- Imprimir lista de motorista')


def menu_viagens():
    print('Opções o gerenciamento de viagens\n')
    print('\t3.0- voltar para o gerenciamento\n'
          '\t3.1- Cadastrar novo viagem\n'
          '\t3.2- Editar viagem\n'
          '\t3.3- Imprimir viagens\n')


def menu_veiculo():
    print('Opções o gerenciamento de veiculos\n')
    print('\t2.0- Volte para o menu de gerenciamento\n'
          '\t2.1- Cadastrar novo veiculo\n'
          '\t2.2- Pesquisar veiculo\n'
          '\t2.3- Editar veiculo\n'
          '\t2.4- Ver quilometragem\n'
          '\t2.5- Deletar veiculo\n'
          '\t2.6- Imprimir lista de veiculos\n')


def cadastrar_motora():
    cpf = input('informe o cpf do motorista')
    aux_motorista = motoristas.get(cpf)
    if aux_motorista:
        return print('cpf ja cadastrado tente de novo')
    else:
        nome = input('informe o nome do motorista')
        cnh = input('informe a CNH do motorista')
        rg = input('informe o RG do motorista')

        motorista = {'nome': nome, 'cpf': cpf, 'rg': rg, 'cnh': cnh}
        motoristas[cpf] = motorista
    return


def busca_motorista(cpf):
    aux_motorista = motoristas.get(cpf)
    if aux_motorista:
        return aux_motorista
    else:
        return print('motorista nao encontrado')


def editar_motorista(cpf):
    aux_motorista = motoristas.get(cpf)
    if aux_motorista:
        CPF = input('informe o cpf do motorista')
        aux_motorista['cpf'] = CPF
        aux_motorista['nome'] = input('informe o nome do motorista')
        aux_motorista['cnh'] = input('informe a CNH do motorista')
        aux_motorista['rg'] = input('informe o rg do motorista')

    if cpf != CPF:
        motoristas[CPF] = motoristas.pop(cpf)

    else:
        print('motorista nao encontrado')


def demitir(cpf):
    aux_motorista = motoristas.get(cpf)
    if aux_motorista:
        aux_motorista = motoristas.pop(cpf)
        del aux_motorista
        print('motorista demitido')
    else:
        return print('motorista nao encontrado')


def cadastrar_veiculo():
    placa = input('informe a placa')
    aux_veiculo = veiculos.get(placa)
    if aux_veiculo:
        return print('veiculo ja cadastrado! Tente novamente!')
    else:
        marca = input('informe a marca do veiculo')
        ano = input('informe o ano do veiculo')
        chassi = input('informe o número do chassi')
        cor = input('informe a cor do veiculo')
        km = input('informe a quilometragem do veiculo')

        veiculo = {'marca': marca, 'ano': ano, 'placa': placa, 'chassi': chassi, 'cor': cor, 'km': km}
        veiculos[placa] = veiculo
        return


def busca_veiculo(placa):
    aux_veiculo = veiculos.get(placa)
    if aux_veiculo:
        return aux_veiculo
    else:
        return print('Veiculo nao encontrado!')


def editar_veiculo(placa):
    aux_veiculo = veiculos.get(placa)
    if aux_veiculo:
        PLACA = input('informe a placa do veiculo')
        aux_veiculo['placa'] = PLACA
        aux_veiculo['marca'] = input('informe a marca do veiculo')
        aux_veiculo['ano'] = input('informe o ano do veiculo ')
        aux_veiculo['chassi'] = input('informe o número do chassi')
        aux_veiculo['cor'] = input('informe a cor do veiculo')
        aux_veiculo['km'] = float(input('informe a quilometragem'))

    if placa != PLACA:
        veiculos[PLACA] = veiculos.pop(placa)
    else:
        print('veiculo nao encontrado')


def deletar_veiculo(placa):
    aux_veiculo = veiculos.get(placa)
    if aux_veiculo:
        aux_veiculo = veiculos.pop(placa)
        del aux_veiculo
        print('veiculo fora da frota!')
    else:
        return print('veiculo nao encontrado!')


def print_km(placa):
    aux_veiculo = veiculos.get(placa)
    if aux_veiculo:
        print('Quilometragem do veiculo ', aux_veiculo['km'])
    else:
        return print('veiculo nao encontrado!')


def cadastrar_viagem():
    codigo = input('informe o codigo da viagem')
    aux_viagem = viagens.get(codigo)
    if aux_viagem:
        return print('viagem ja agendada, tente novamente!')
    else:
        destino = input('informe o destino da viagem')
        origem = input('informe a origem')
        transporte = input('informe a placa do veiculo')
        motora = input('informe o  cpf do motorista')
        distância = float(input('informe a distância da viagem'))

        viagem = {'codigo': codigo, 'destino': destino, 'origem': origem, 'veiculo': transporte, 'motorista': motora,
                  'distância': distância}
        viagens[codigo] = viagem

        aux_cont_m = cont_motorista2.get(motora)
        if aux_cont_m:
            aux_cont_m['motorista'] = motora
            aux_cont_m['distância'] += distância
            aux_cont_m['quant'] += 1
        else:
            cont_motorista = {'motorista': motora, 'distância': distância, 'quant': 1}
            cont_motorista2[motora] = cont_motorista

        aux_veiculo1 = veiculos.get(transporte)
        if aux_veiculo1:
            km = aux_veiculo1['km']
            pass
        else:
            return print('voce digitou um veiculo fora da frota')

        aux_veiculo2 = cont_veciculo2.get(transporte)
        if aux_veiculo2:
            aux_veiculo2['placa'] = transporte
            aux_veiculo2['distância'] = distância + km
            aux_veiculo2['quant'] += 1
        else:
            cont_veciculo = {'placa': transporte, 'distância': distância, 'quant': 1}
            cont_veciculo2[transporte] = cont_veciculo
        return


def editar_viagem(codigo):
    aux_viagem = viagens.get(codigo)
    if aux_viagem:
        CODIGO = input('informe o código da viagem!')
        aux_viagem['destino'] = input('inform o novo destino da viagem!')
        aux_viagem['codigo'] = CODIGO
        aux_viagem['origem'] = input('informe a origem da viagem')
        aux_viagem['veiculo'] = input('informe a placa do veiculo')
        aux_viagem['motorista'] = input('informe o cpf do motorista')
        aux_viagem['distância'] = input('inform a distância da viagem')

    if codigo != CODIGO:
        viagens[CODIGO] = viagens.pop(codigo)

    else:
        return print('Viagem não agendada!')


def cadastrar_abastecimento():
    motora = input('informe o cpf do motorista que fez o abastecimento!')
    aux_abastecimento = motoristas.get(motora)
    if aux_abastecimento:
        placa = input('Informe a placa do veiculo a ser abastecido')
        data = input('Informe a data do abastecimento (use o formato DD/MM/AA)')
        litros = float(input('informe a quantidade em litros'))
        valor = float(input('informe o pago no abastecimento!'))
        abastecimento = {'placa': placa, 'data': data, 'litros': litros, 'valor': valor, 'motorista': motora}
        abastecimentos[placa] = abastecimento
        return
    else:
        return print('Motorista nao encontrado!')


def cadastrar_manutenção():
    placa = input('informe a placa do veiculo')
    aux_manutenção = veiculos.get(placa)
    if aux_manutenção:
        tipo = input('qual o tipo de manutenção realizada?')
        data = input('qual da manutenção realizada?')
        custo = float(input('qual o valor total da manutenção?'))

        manutenção1 = {'placa': placa, 'tipo': tipo, 'data': data, 'custo': custo}
        manutenção2[placa] = manutenção1


def conta_motorista():
    quantidade = 0
    for dicionário in cont_veciculo2.values():
        if quantidade <= dicionário['quant']:
            quantidade = dicionário['quant']
        else:
            continue
    return quantidade


def conta_motorista_km():
    quantidade = 0
    for dicionário in cont_motorista2.values():
        if quantidade <= dicionário['distância']:
            quantidade = dicionário['motorista']
        else:
            continue
    return quantidade


def conta_veiculo():
    quantidade = 0
    for dicionário in cont_veciculo2.values():
        if quantidade <= dicionário['quant']:
            quantidade = dicionário['quant']
        else:
            continue
    return quantidade


def conta_veiculo_km():
    quantidade = 0
    for dicionário in cont_veciculo2.values():
        if quantidade <= dicionário['distância']:
            quantidade = dicionário['distância']
        else:
            continue
    return quantidade


def total_manutenção():
    total_m = 0
    for dicionário in manutenção2.values():
        total_m = total_m + dicionário['custo']
    return total_m


def total_abastecimento():
    valor_total = 0
    for dicionário in abastecimentos.values():
        valor_total = valor_total + dicionário['valor']
    return valor_total


def relatorio():
    quant_motoristas = len(motoristas)
    quant_veiculos = len(veiculos)
    total_A = total_abastecimento()
    total_M = total_manutenção()
    maior_motorista_km = conta_motorista_km()
    maior_motorista = conta_motorista()
    maior_veiculo = conta_veiculo()
    maior_veiculo_km = conta_veiculo_km()
    print('-' * 20, 'relatorio', '-' * 20)
    print('|1-Quantidade de motoristas    {}|\n'
          '|2-Quantidade de Veiculos      {}|\n'
          '|3-preço total abastecimentos  {}|\n '
          '|4-Preço total manutenção      {}|\n'
          '|5-Motorista com mais viagens  {}|\n'
          '|6-Motorista com mais km       {}|\n'
          '|7-Veiculo com mais viagens    {}|\n'
          '|8-Veiculo com mais km         {}|\n'.format(quant_motoristas, quant_veiculos, total_A, total_M,
                                                        maior_motorista, maior_motorista_km, maior_veiculo,
                                                        maior_veiculo_km))


cont_motorista = {}
cont_motorista2 = {}

cont_veciculo = {}
cont_veciculo2 = {}

motorista = {}
motoristas = {"111": {"nome": "François", "CPF": "111", "RG": "223212", "CNH": "34221"},
              "222": {"nome": "Ana", "CPF": "222", "RG": "223212", "CNH": "34221"},
              "333": {"nome": "MAria", "CPF": "333", "RG": "223212", "CNH": "34221"}}

veiculo = {}
veiculos = {"jc": {"marca": "Fiat", "modelo": "UNO", "ano": "2003",
                   "placa": "jc", "chassi": "36563652", "cor": "Branco", "km": 500},
            "lv": {"marca": "Fiat", "modelo": "Toro", "ano": "2003",
                   "placa": "lv", "chassi": "36563652", "cor": "Branco", "km": 500},
            "GF": {"marca": "Fiat", "modelo": "Argo", "ano": "2003",
                   "placa": "lv", "chassi": "36563652", "cor": "Branco", "km": 500}}

viagem = {}
viagens = {}

abastecimento = {}
abastecimentos = {}

manutenção1 = {}
manutenção2 = {}
nub = -1
op2 = -1
op3 = -1
op4 = -1
op5 = -1
op6 = -1
while nub != 0:
    menu()
    op = int(input("O que deseja fazer ??"))
    op2 = -1
    op3 = -1
    op4 = -1
    op5 = -1
    op6 = -1
    if op == 0:
        print('programa encerrado!')
        nub = 0
        pass
    elif op == 1:
        menu_motora()
        while op2 != 0:
            op_m = int(input('O que fazer ?'))
            if op_m == 0:
                op2 = 0
                pass
            elif op_m == 1:
                cadastrar_motora()
                pass
            elif op_m == 2:
                cpf = input('informe o cpf do motorista que deseja achar')
                motora = busca_motorista(cpf)
                print(motora)
                pass
            elif op_m == 3:
                cpf = input('informe o cpf do motorista para editar os dados')
                editar_motorista(cpf)
                pass
            elif op_m == 4:
                cpf = input('informe o cpf do motorista que deseja demitir')
                demitir(cpf)
                pass
            elif op_m == 5:
                for chave, motorista in motoristas.items():
                    print(chave + ":")
                    for subchave, valor in motorista.items():
                        print("    " + subchave + ": " + valor)

                pass

    elif op == 2:
        while op3 != 0:
            menu_veiculo()
            op_v = int(input('o que fazer nos veiculos?'))
            if op_v == 0:
                op3 = 0
                pass
            elif op_v == 1:
                cadastrar_veiculo()
                pass
            elif op_v == 2:
                placa = input('informe a placa para buscar veiculo')
                mostre = busca_veiculo(placa)
                print(mostre)
                pass
            elif op_v == 3:
                placa = input('informe a placa para editar dados do veiculo')
                editar_veiculo(placa)
                pass
            elif op_v == 4:
                placa = input('informe a placa para ver a quilometragem !')
                print_km(placa)
                pass
            elif op_v == 5:
                placa = input('informe a placa do veiculo para o tirar da frota')
                deletar_veiculo(placa)
                pass
            elif op_v == 6:
                for chave, veiculo in veiculos.items():
                    print(chave + ":")
                    for subchave, valor in veiculo.items():
                        if isinstance(valor, float):
                            print("    {} : {:.2f}".format(subchave, valor))
                        else:
                            print("    {} : {}".format(subchave, valor))
                pass

    elif op == 3:
        while op4 != 0:
            menu_viagens()
            op_vg = int(input('gerenciar viagens! o que deseja fazer?'))

            if op_vg == 0:
                op4 = 0
                pass
            elif op_vg == 1:
                cadastrar_viagem()
                pass
            elif op_vg == 2:
                codigo = input('informe o codigo da viagem que deseja editar')
                editar_viagem(codigo)
                pass
            elif op_vg == 3:
                for chave, viagem in viagens.items():
                    print(chave + ":")
                    for subchave, valor in viagem.items():
                        if isinstance(valor, float):
                            print("    {} : {:.2f}".format(subchave, valor))
                        else:
                            print("    {} : {}".format(subchave, valor))

                print(cont_motorista2)
                print(cont_veciculo2)
                pass
    elif op == 4:
        while op5 != 0:
            menu_abastecimento()
            op_ab = int(input('o que deseja fazer?'))

            if op_ab == 0:
                op5 = 0
                pass
            elif op_ab == 1:
                cadastrar_abastecimento()
                pass
            elif op_ab == 2:
                for chave, abastecimento in abastecimentos.items():
                    print('-' * 30)
                    print(chave + ":")
                    for subchave, valor in abastecimento.items():
                        print("    " + subchave + ": " + valor)
                pass
    elif op == 5:
        while op6 != 0:
            menu_manutenção()
            op_mm = int(input(' o que deseja fazer ?'))
            if op_mm == 0:
                op6 = 0
                pass
            elif op_mm == 1:
                cadastrar_manutenção()
                pass
            elif op_mm == 2:
                for chave, manutenção1 in manutenção2.items():
                    print('-' * 30)
                    print(chave + ":")
                    for subchave, valor in manutenção1.items():
                        print("    " + subchave + ": " + valor)
                pass
    elif op == 6:
        relatorio()
