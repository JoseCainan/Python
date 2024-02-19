# biblioteca digite no CMD - pip install num2words
# o comando acima instala a biblioteca no pc
from num2words import num2words

op = -1
while op != 0:

    print('\t|0- encerrar atividade     |'
          '\n\t|1-Intercessor e sucessor! |'
          '\n\t|2-Dobro - triplo - raiz   |'
          '\n\t|3-Média de duas notas     |'
          '\n\t|4-Centímetros e Milímetros|'
          '\n\t|5-Tabuada                 |'
          '\n\t|6-Conversão real e dólar  |'
          '\n\t|7-Área e tinta para pintar|'
          '\n\t|8-Salário mais 15%        |'
          '\n\t|9-Celsius para fahrenheit |'
          '\n\t|10-Números por extenso    |\n')

    num = int(input('Escolha uma questão!'))

    if num == 0:
        print('Atividade encerrada, volte sempre!\n')
        op = 0

    elif num == 1:
        número = int(input('informe um número'))
        aux = número + 1
        aux2 = número - 1
        print('Antecessor: {}\nSucessor: {}'.format(aux2, aux))
        aux2 = 0
        aux = 0

    elif num == 2:
        número = int(input('informe um número'))
        aux = número * 2
        aux2 = número * 3
        raiz = número**(1/2)
        print('Dobro: {}\nTriplo: {}\nRaiz quadrada: {}'.format(aux, aux2, raiz))
        aux2 = 0
        aux = 0

    elif num == 3:
        nota1 = float(input('Informe a nota 1 !'))
        nota2 = float(input('Informe a nota 2 !'))
        media = (nota1 + nota2)/2
        if media >= 7:
            print('aluno aprovado com média', media)
        else:
            print('aluno reprovado com média', media)

    elif num == 4:
        metros = float(input('Informe um valor em metros !'))
        cent = metros*100
        mili = metros*1000
        print('metros: {}\ncentímetros: {}\nmilímetros: {}\n'.format(metros, cent, mili))

    elif num == 5:
        aux = int(input('informe um número!'))
        for x in range(0, 11):
            print(aux, 'X', x, '=', aux*x)
        aux = 0

    elif num == 6:
        dinheiro = float(input('Quantos reais você tem ?'))
        dólar = dinheiro/3.27
        print('Você pode comprar', int(dólar))
        print('\n')

    elif num == 7:
        base = float(input('Informe a largura da parede !'))
        altura = float(input('Informe a altura da parede'))
        área = base*altura
        tinta = área/2
        print('área: {}\nQuantidade necessária: {}\n'.format(área, tinta))

    elif num == 8:
        salário = float(input('informe o seu salario'))
        acres = salário + (salário*15/100)
        print('Seu novo salário é:{:.2f}'.format(acres), '\n')

    elif num == 9:
        celsius = float(input('Informe a temperatura em celsius!'))
        fahrenheit = ((9 * celsius) / 5) + 32
        print('A temperatura de {}°C em fahrenheit é: {}°F'.format(celsius, fahrenheit))

    elif num == 10:
        aux = float(input('informe um número !'))
        aux2 = num2words(aux, lang='pt_BR')
        print(f'{aux}: {aux2}\n')

