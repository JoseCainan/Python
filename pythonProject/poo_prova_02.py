from classes_percistencias import*

aux_mot = {}

Dic_motorista =  {"111": {"nome": "François", "CPF": "111", "RG": "223212", "CNH": "34221",},
              "222": {"nome": "Ana", "CPF": "222", "RG": "223212", "CNH": "34221"},
              "333": {"nome": "Maria", "CPF": "333", "RG": "223212", "CNH": "34221"}}

Dic_veiculos = {"jc": {"marca": "Fiat", "modelo": "UNO", "ano": "2003",
                   "placa": "jc", "chassi": "36563652", "cor": "Branco", "km": 500},
            "lv": {"marca": "Fiat", "modelo": "Toro", "ano": "2003",
                   "placa": "lv", "chassi": "36563652", "cor": "Branco", "km": 500},
            "GF": {"marca": "Fiat", "modelo": "Argo", "ano": "2003",
                   "placa": "lv", "chassi": "36563652", "cor": "Branco", "km": 500}}

Dic_viagens = {}

Dic_abastecimento = {}

Dic_manutenção = {}


def total_man():
    valor_total = 0
    for aux in Dic_manutenção.values():
        valor_total = valor_total + aux["custo"]
    return valor_total
def total_abs():
    valor_total = 0
    for aux in Dic_abastecimento.values():
        valor_total = valor_total + aux["valor"]
    return valor_total

def relatorio():
    quant_motoristas = len(Dic_motorista)
    quant_veiculos =  len(Dic_veiculos)
    total_manutenção = total_man()
    total_abast = total_abs()
    print('-' * 20, 'relatorio', '-' * 20)
    print('|1-Quantidade de motoristas    {}|\n'
          '|2-Quantidade de Veiculos      {}|\n'
          '|3-preço total abastecimentos  {}|\n '
          '|4-Preço total manutenção      {}|\n'.format(quant_motoristas, quant_veiculos, total_abast, total_manutenção))


def maior_Km_mot():
    maior_mot_km = None
    maiormot = 0
    for motora, aux in aux_mot.items():
        if aux_mot["km_rodados"] > maiormot:
            maiormot = aux["km_rodados"]
            maior_mot_km = motora
    print("o motorista que percorreu maior Km: {}".format(maior_mot_km))

def mais_viagens():
    maior_num = 0
    mot_mais = 0
    for motora, aux in aux_mot.items():
        if aux["cont_num"] > maior_num:
            maior_num = aux["cont_num"]
            mot_mais = motora
    print("o motorista que fez mais viagens foi: {}".format(mot_mais))
class Motoristas():
    def __init__(self, nome, cpf, rg, cnh, cont_km = 0):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.cnh = cnh
        self.cont_km = cont_km

    def adicionar(self, motorista):
        nome = motorista.nome
        cpf = motorista.cpf
        rg = motorista.rg
        cnh = motorista.cnh
        cont_km = motorista.cont_km
        Dic_motorista[cpf] = {"nome": nome, "cpf": cpf, "rg": rg, "cnh": cnh, "cont_km": cont_km}

    def editar(self, cpf, new_nome, new_rg, new_cnh):
        aux_motorista = Dic_motorista.get(cpf)
        if aux_motorista:
            aux_motorista["nome"] = new_nome
            aux_motorista["rg"] = new_rg
            aux_motorista["cnh"] = new_cnh
        else:
            return print('motorista nao encontrado')

    def busca_motorista(self):
        aux_motorista = Dic_motorista.get(input('informe o cpf do para buscar!'))
        if aux_motorista:
            return aux_motorista["nome"]
        else:
            return print('motorista nao encontrado')

    def deletar(self, cpf):
        motorista_aux = Dic_motorista.get(cpf)
        if motorista_aux:
            motorista_aux = Dic_motorista.pop(cpf)
            del motorista_aux
            print("Motorista demitido")
        else:
            return  print("motorista não encontrado !")

    def imprime_motoras(self):
        for chave, motorista in Dic_motorista.items():
            print(chave + ":")
            for subchave, valor in motorista.items():
                print("    " , subchave , ": " , valor)
            print('-'*30)

class Veiculos():
    def __init__(self, placa, marca, modelo, ano, n_chassi, cor, kilom):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.n_chassi = n_chassi
        self.cor = cor
        self.kilom = kilom

    def adicinar(self,veiculo):
        placa = veiculo.placa
        marca = veiculo.marca
        modelo = veiculo.modelo
        ano = veiculo.ano
        n_chassi = veiculo.n_chassi
        cor = veiculo.cor
        kilom = veiculo.kilom

        Dic_veiculos[placa] = {"placa": placa, "marca": marca, "modelo": modelo,
                               "ano": ano, "n_chassi": n_chassi, "cor": cor, "kilom": kilom}

    def editar_vec(self,placa, new_placa, new_marca, new_ano, new_n_chassi, new_cor, new_kilom):
        aux_veiculos = Dic_veiculos.get(placa)
        if aux_veiculos:
            aux_veiculos["placa"] = new_placa
            aux_veiculos["marca"] = new_marca
            aux_veiculos["ano"] = new_ano
            aux_veiculos["n_chassi"] = new_n_chassi
            aux_veiculos["cor"] = new_cor
            aux_veiculos["kilom"] = new_kilom
        else:
            return print('veiculo nao encontrado')

    def buscar_veiculo(self,placa):
        aux_veiculo = Dic_veiculos.get(placa)
        if aux_veiculo:
            print(aux_veiculo)
            return aux_veiculo
        else:
            return print('veiculo nao encontrado')

    def imprime_veiculos(self):
        for chave, veiculo in Dic_veiculos.items():
            print(chave + ":")
            for subchave, valor in veiculo.items():
                print("    " , subchave , ": " , valor)
            print('-'*30)

    def mais_km(self):
        maior = 0
        vec_maior = None
        for vec, aux in Dic_veiculos.items():
            if aux["km"] > maior:
                maior = aux["km"]
                vec_maior = vec
        print("O veiculo com maior quilometragem é {}".format(vec_maior))

    def deletar_vec(self, placa):
        veiculo_aux = Dic_veiculos.get(placa)
        if veiculo_aux:
            veiculo_aux = Dic_veiculos.pop(placa)
            del veiculo_aux
            print("veiculo removido da frota")
        else:
            return  print("veiculo ja fora da frota !")


class Viagens():
    def __init__(self, codigo, motorista, placa_v, destino, origem, distância):
        self.codigo = codigo
        self.motorista = motorista
        self.placa_v = placa_v
        self.destino = destino
        self.origem = origem
        self.distância = distância

    def adicionar_viagens(self,viagem):
        codigo = viagem.codigo
        motorista = viagem.motorista
        placa_v = viagem.placa_v
        destino = viagem.destino
        origem = viagem.origem
        distância = viagem.distância

        Dic_viagens[codigo] = {"codigo": codigo, "motorista": motorista, "placa_v": placa_v,
                               "destino": destino, "origem": origem, "distância": distância}

        if motorista in Dic_motorista:
            if motorista in aux_mot:
                aux_mot[motorista]["km_rodados"] += distância
            else:
                aux_mot[motorista] = {"cpf": motorista, "km_rodados": distância}

            if motorista in aux_mot:
                aux_mot[motorista]["cont_num"] += 1
        else:
            return print("motorista nao existe !")

        if placa_v in Dic_veiculos:
            Dic_veiculos[placa_v]["km"] += distância
        else:
            return print("veiculo nao existe !")

    def editar_viagens(self,code):
        aux_viagens = Dic_viagens.get(code)
        if aux_viagens:
            aux_viagens["codigo"] = input('informe o novo codigo')
            aux_viagens["motorista"] = input("informe o cpf do motorista")
            aux_viagens["placa_v"] = input("informe a placa do veiculo")
            aux_viagens["destino"] = input("informe o destino")
            aux_viagens["origem"] = input("informe a origem")
            aux_viagens["distância"] = input("informe a distância")
        else:
            return print('viagem  nao cadastrada')

    def buscar_viagens(self, codigo):
        aux_viagens = Dic_viagens.get(codigo)
        if aux_viagens:
            print(aux_viagens)
            return aux_viagens
        else:
            return print('veiculo nao encontrado')

    def imprimir_viagens(self):
        for chave, viagens in Dic_viagens.items():
            print(chave , ":")
            for subchave, valor in viagens.items():
                print("    ", subchave, ": ", valor)
            print('-' * 30)


class Abastecimento:
    def __init__(self, motorista, placa_v, data, quantidade, valor):
        self.motorista = motorista
        self.placa_v = placa_v
        self.data = data
        self.quantidade = quantidade
        self.valor = valor

    def adicionar_ab(self, abastecimento):
        motorista = abastecimento.motorista
        placa_v = abastecimento.placa_v
        data = abastecimento.data
        quantidade = abastecimento.quantidade
        valor = abastecimento.valor

        Dic_abastecimento[motorista] = {"motorista": motorista, "placa_v": placa_v,
                                          "data": data, "quantidade": quantidade,"valor": valor}

    def imprimir_ab(self):
        for chave, abas in Dic_abastecimento.items():
            print(chave + ":")
            for subchave, valor in abas.items():
                print("    " , subchave , ": " , valor)
            print('-'*30)



class Manutenção:

    def __init__(self, placa_v, data, tipo_m, custo):
        self.placa_v = placa_v
        self.data = data
        self.tipo_m = tipo_m
        self.custo = custo

    def adicionar_man(self,manutenção):
        placa_v = manutenção.placa_v
        data = manutenção.data
        tipo_m = manutenção.tipo_m
        custo =  manutenção.custo

        Dic_manutenção[placa_v] = {"placa_v": placa_v, "data": data, "tipo_m": tipo_m, "custo": custo}
    def imprimir_m(self):
        for chave, man in Dic_manutenção.items():
            print(chave + ":")
            for subchave, valor in man.items():
                print("    " , subchave , ": " , valor)
            print('-'*30)


