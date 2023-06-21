from classes_percistencias import*
from poo_prova_02 import*
import json

with open('Motora_arc.json', 'w') as write_file:
    json.dump(Dic_motorista, write_file, indent=4)

with open('Veiculo_arc.json', 'w') as write_file:
    json.dump(Dic_veiculos, write_file, indent=4)

with open('Viagens_arc.json', 'w') as write_file:
    json.dump(Dic_viagens, write_file, indent=4)

with open('Manutenção_arc.json', 'w') as write_file:
    json.dump(Dic_manutenção, write_file, indent=4)

with open('Abastecimento_arc.json', 'w') as write_file:
    json.dump(Dic_abastecimento, write_file, indent=4)
def menu():
    print('-'*20, 'MENU', '-'*20)
    print('|0-Sair do programa            |\n'
          '|1-Gerenciamento de Motoristas |\n'
          '|2-Gerenciamento de Veiculos   |\n'
          '|3-Gerenciamento de Viagem     |\n'
          '|4-Abastecimento da frota      |\n'
          '|5-Manutenção dos Veiculos     |\n'
          '|6-Imprimeir relatorio         |\n')

def menu_motora():
    print('Opções o gerenciamento de motoristas\n')
    print('\t|1.0- volte para o menu de gerenciameto|\n'
          '\t|1.1- Cadastrar novo motorista         |\n'
          '\t|1.2- Pesquisar Motorista              |\n'
          '\t|1.3- Editar motorista                 |\n'
          '\t|1.4- Deletar Motorista                |\n'
          '\t|1.5- Imprimir lista de motorista      |\n')

def menu_viagens():
    print('Opções o gerenciamento de viagens\n')
    print('\t|3.0- voltar para o gerenciamento   |\n'
          '\t|3.1- Cadastrar novo viagem         |\n'
          '\t|3.2- Editar viagem                 |\n'
          '\t|3.3- Imprimir viagens              |\n'
          '\t|3.4- Buscar viagem                 |\n')

def menu_veiculo():
    print('Opções o gerenciamento de veiculos           |\n')
    print('\t|2.0- Volte para o menu de gerenciamento   |\n'
          '\t|2.1- Cadastrar novo veiculo               |\n'
          '\t|2.2- Pesquisar veiculo                    |\n'
          '\t|2.3- Editar veiculo                       |\n'
          '\t|2.4- Ver quilometragem                    |\n'
          '\t|2.5- Deletar veiculo                      |\n'
          '\t|2.6- Imprimir lista de veiculos           |\n')

def menu_abastecimento():
    print('Opções o gerenciamento de abastecimento\n')
    print('\t|4.0- voltar para o gerenciamento\n'
          '\t|4.1- Cadastrar novo abastecimento\n'
          '\t|4.2- Imprimir abastecimentos\n')

def menu_manutenção():
    print('\t|5.0- voltar ao gerenciamento\n'
          '\t|5.1- Cadastrar nova manutenção\n'
          '\t|5.2- Imprimir manutenção\n')
nub = -1


while nub != 0:
    menu()
    op = int(input('O que deseja fazer ?'))
    op2 = -1
    op3 = -1
    op4 = -1
    op5 = -1
    op6 = -1

    if op == 0:
        print('programa encerrado !')
        nub = 0
        pass
    elif op == 1:
        menu_motora()
        while op2 != 0:
            op_m = int(input('O que deseja fazer?'))
            if op_m == 0:
                op2 = 0
                pass
            elif op_m == 1:
                nome_mot = input("informe o nome do motorista")
                cpf_mot = input("informe o cpf do motorista")
                rg_mot = input("informe o rg o motorista")
                cnh_mot = input("informe a cnh do motorista")
                aux_motorista = Motoristas(nome_mot, cpf_mot, rg_mot, cnh_mot)
                aux_motorista.adicionar(aux_motorista)
                # colocando o dicionario no arquivo
                with open('Motora_arc.json', 'w') as write_file:
                    json.dump(Dic_motorista, write_file, indent=4)
                pass

            elif op_m == 2:
                motorista = Motoristas(None, None, None, None)
                print("o motorista é {}".format( motorista.busca_motorista()))
                pass
            elif op_m == 3:
                cpf = input("informe o cpf do motorista que deseja editar")
                new_nome = input("informe o novo nome !")
                new_rg = input("informe o novo rg !")
                new_cnh = input('informe a nova cnh !')

                aux_motorista = Motoristas(None, None, None, None)
                aux_motorista.editar(cpf, new_nome, new_rg, new_cnh)
                pass
            elif op_m == 4:
                cpf_def = input('informe o cpf do motorista que deseja demitir')
                motorista = Motoristas(None, None, None, None)
                motorista.deletar(cpf_def)
                # alterando o arquivo
                with open('Motora_arc.json', 'w') as write_file:
                    json.dump(Dic_motorista, write_file, indent=4)
                pass
            elif op_m == 5:
                motorista = Motoristas(None, None, None, None)
                motorista.imprime_motoras()
                pass
    elif op == 2:
        while op3 != 0:
            menu_veiculo()
            op_v = int(input('O que deseja fazer nos veiculos'))
            if op_v == 0:
                op3 = 0
                pass
            elif op_v == 1:
                placa_vec = input("informe a placa do veiculo")
                marca_vec = input("informe a marca do veiculo")
                modelo_vec = input("informe o modelo do veiculo")
                ano_vec = input("informe o ano do veiculo")
                chassi = input("informe o número do chassi")
                cor_vec = input("informe a cor do veiculo")
                kilom_vec = input("informe a quilometragem")

                aux_veiculo = Veiculos(placa_vec, marca_vec, modelo_vec, ano_vec, chassi,cor_vec, kilom_vec)
                aux_veiculo.adicinar(aux_veiculo)
                # criando arquivo de veiculo
                with open('Veiculo_arc.json', 'w') as write_file:
                    json.dump(Dic_veiculos, write_file, indent=4)
                pass
            elif op_v == 2:
                placa = input('informe a placa do veiculo que deseja buscar')
                aux_veiculo = Veiculos(None, None, None, None, None, None, None)
                aux_veiculo.buscar_veiculo(placa)
                pass
            elif op_v == 3:
                aux_veiculo = Veiculos(None, None, None, None, None, None, None)
                placa = input("informe a placa do veiculo para poder editar os dados")
                nova_placa = input("informe a nova placa do veiculo")
                nova_marca = input("informe a nova marca")
                novo_ano = input("informe o novo ano ")
                novo_chassi = input("informe o numero do chassi")
                nova_cor = input("informe a nova cor")
                nova_kilom = input("informe a quilometragem")
                aux_veiculo.editar_vec(placa,nova_placa,nova_marca,novo_ano,
                                       novo_chassi,nova_cor,nova_kilom)
                pass
            elif op_v == 4:
                placa = input('informe a placa do veiculo que deseja ver a quilometragem')
                kilom_vec = Dic_veiculos.get(placa)
                if kilom_vec:
                    print("Quilometragem do veiculo = {}".format(kilom_vec["kilom"]))
                else:
                    print("veiculo nao encontrado")
                pass
            elif op_v == 5:
                aux_veiculo = Veiculos(None, None, None, None, None, None, None)
                placa = input("informe a placa do veiculo que deseja remover da frota")
                aux_veiculo.deletar_vec(placa)
                # alterando o arquivo veiculo
                with open('Veiculo_arc.json', 'w') as write_file:
                    json.dump(Dic_veiculos, write_file, indent=4)
                pass
            elif op_v == 6:
                aux_veiculo = Veiculos(None, None, None, None, None, None, None)
                aux_veiculo.imprime_veiculos()
                pass
    elif op == 3:
        while op4 != 0:
            menu_viagens()
            op_vg = int(input("Gerenciar viagens! o que deseja fazer?"))

            if op_vg == 0:
                op4 = 0
                pass
            elif op_vg == 1:
                cod = input("informe o codigo da viagem")
                motorista = int(input("informe cpf do motorista"))
                placa_vec = input("informe a placa do veiculo")
                dest = input("informe o destino")
                orig = input("informe a origem da viagem")
                distance = int(input("informe a distancia da viagem"))

                aux_viagens = Viagens(cod, motorista, placa_vec, dest, orig, distance)
                aux_viagens.adicionar_viagens(aux_viagens)
                # criando arquivo de viagens
                with open('Viagens_arc.json', 'w') as write_file:
                    json.dump(Dic_viagens, write_file, indent=4)
                pass
            elif op_vg == 2:
                aux_viagens = Viagens(None, None, None, None, None, None)
                cod = input("informe o codigo da viagem para edita-la")
                aux_viagens.editar_viagens(cod)
                pass
            elif op_vg == 3:
                aux_viagens = Viagens(None, None, None, None, None, None)
                aux_viagens.imprimir_viagens()
                pass
            elif op_vg == 4:
                aux_viagens = Viagens(None, None, None, None, None, None)
                cod = input("informe o codigo da viagem para busca-la")
                aux_viagens.buscar_viagens(cod)
                pass
    elif op == 4:
        while op5 != 0:
            menu_abastecimento()
            op_ab = int(input("o que deseja fazer em abastecimento ?"))

            if op_ab == 0:
                op5 = 0
                pass
            elif op_ab == 1:
                motora = input("informe o cpf do motorista que fez o abastecimento")
                placa_vv = input("informe a placa do veiculo abastecido")
                data = input("informe a data do abastecimento")
                quant = input("informe a quantidade em litros")
                valor = float(input("informe o valor total do abastecimento"))

                abastecimento = Abastecimento(motora, placa_vv, data, quant, valor)
                abastecimento.adicionar_ab(abastecimento)
                #criando arquivo de abastecimento
                with open('Abastecimento_arc.json', 'w') as write_file:
                    json.dump(Dic_abastecimento, write_file, indent=4)
                pass
            elif op_ab == 2:
                abastecimento = Abastecimento(None, None, None, None, None)
                abastecimento.imprimir_ab()
    elif op == 5:
        while op6 != 0:
            menu_manutenção()
            op_mm = int(input("o que deseja fazer em manutenção"))
            if op_mm == 0:
                op6 =0
                pass
            elif op_mm == 1:
                placa_vv = input("informe a placa do veiculo para manutenção")
                data = input("informe a data da manutenção")
                tipo_m = input("informe o tipo de manutenção")
                custo = int(input("informe o custo da manutenção"))
                manutenção = Manutenção(placa_vv, data, tipo_m, custo)
                manutenção.adicionar_man(manutenção)
                # criando o arquuivo de manutenção
                with open('Manutenção_arc.json', 'w') as write_file:
                    json.dump(Dic_manutenção, write_file, indent=4)
                pass
            elif op_mm == 2:
                manutenção = Manutenção(None, None, None, None)
                manutenção.imprimir_m()
                pass
    elif op == 6:
        relatorio()
        pass





