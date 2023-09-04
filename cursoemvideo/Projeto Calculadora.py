from tkinter import *


raiz = Tk()
raiz.title('Calculadora Cientifíca ')
raiz.geometry('408x355')
raiz.minsize(408,355)
raiz.maxsize(1008,955)

raiz.configure(background='#282828')

numero1 = ''
divisao = FALSE
multiplica = FALSE
mais = FALSE
menos = FALSE


ent = Entry(raiz, width=15, borderwidth=4, relief=GROOVE, fg='#FFFFFF', bg='#FFC0CB', font=('futura', 25, 'bold'), justify=CENTER)
ent.grid(
    row= 0,
    column= 0,
    columnspan=4,
    pady= 2
)
#funçoes de operadores
def botao_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = ent.get()
    ent.delete(0, END)
    return

def botao_multiplica():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = ent.get()
    ent.delete(0, END)
    return
def botao_menos():
    global numero1
    global menos
    menos = TRUE
    numero1 = ent.get()
    ent.delete(0, END)
    return
def botao_mais():
    global numero1
    global mais
    mais = TRUE
    numero1 = ent.get()
    ent.delete(0, END)
    return
def botao_limpar():
    ent.delete(0, END)
    return
def botao_igual():
    global menos
    global mais
    global multiplica
    global divisao
    numero2 = ent.get()
    ent.delete(0, END)
    if mais == TRUE:
        ent.insert(0, int(numero1) + int(numero2))
        mais = False

    elif menos == TRUE:
        ent.insert(0, int(numero1) - int(numero2))
        menos = FALSE

    elif multiplica == TRUE:
        ent.insert(0, int(numero1) * int(numero2))
        multiplica = FALSE

    elif divisao == TRUE:
        ent.insert(0, int(numero1) / int(numero2))
        divisao = FALSE
    return
def botao_click(num):
    ent.insert(END, num)
    return

b_divide = Button(raiz,
                  text='÷',
                  padx=41,
                  pady=20,
                  command=botao_divisao,
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#FFC0CB',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_divide.grid(row=0,column=4)

#primeira fila
b_um = Button(raiz,
                  text='1',
                  padx=41.5,
                  pady=20,
                  command=lambda: botao_click(1),
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_um.grid(row=1, column=1)

b_dois = Button(raiz,
                  text='2',
                  padx=40,
                  pady=20,
                  command=lambda: botao_click(2),
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_dois.grid(row=1, column=2)


b_tres = Button(raiz,
                  text='3',
                  padx=40,
                  pady=20,
                  command=lambda: botao_click(3),
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_tres.grid(row=1, column=3)

b_multiplica = Button(raiz,
                  text='x',
                  padx=41,
                  pady=20,
                  command= botao_multiplica,
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_multiplica.grid(row=1, column=4)
# segunda fileira

b_quatro = Button(raiz,
                  text='4',
                  padx=41.5,
                  pady=20,
                  command=lambda: botao_click(4),
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_quatro.grid(row=2, column=1)

b_cinco = Button(raiz,
                  text='5',
                  padx=40,
                  pady=20,
                  command=lambda: botao_click(5),
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_cinco.grid(row=2, column=2)

b_seis = Button(raiz,
                  text='6',
                  padx=40,
                  pady=20,
                  command=lambda: botao_click(6),
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_seis.grid(row=2, column=3)


b_menos = Button(raiz,
                  text='-',
                  padx=43,
                  pady=20,
                  command= botao_menos,
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_menos.grid(row=2, column=4)
#terceira fileira

b_sete = Button(raiz,
                  text='7',
                  padx=41.5,
                  pady=20,
                  command=lambda: botao_click(7),
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_sete.grid(row=3, column=1)

b_oito = Button(raiz,
                  text='8',
                  padx=40,
                  pady=20,
                  command=lambda: botao_click(8),
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_oito.grid(row=3, column=2)

b_nove = Button(raiz,
                  text='9',
                  padx=40,
                  pady=20,
                  command=lambda: botao_click(9),
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_nove.grid(row=3, column=3)

b_mais = Button(raiz,
                  text='+',
                  padx=41,
                  pady=20,
                  command= botao_mais,
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_mais.grid(row=3, column=4)
# quarta fileira

b_zero = Button(raiz,
                  text='0',
                  padx=91,
                  pady=20,
                  command=lambda: botao_click(0),
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_zero.grid(row=4, column=2, columnspan=2)

b_limpar = Button(raiz,
                  text='C',
                  padx=40,
                  pady=20,
                  command= botao_limpar,
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_limpar.grid(row=4, column=1)

b_igual = Button(raiz,
                  text='=',
                  padx=41,
                  pady=20,
                  command= botao_igual,
                  fg='#FFFFFF',
                  activebackground='#282828',
                  bg='#320064',
                  activeforeground='#240046',
                  relief=RAISED,
                  font=('futura', 12, 'bold')
                  )
b_igual.grid(row=4, column=4)




raiz.mainloop()