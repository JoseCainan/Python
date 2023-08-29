import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Aceita ?')
root.geometry('600x600')
root.configure(background='#ffcc8d')

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo(
        'te amo, lavineg, vamos tomar aquele açaí de novo :) ?')

def denied():
    button_1.destroy()

margin = Canvas(root, width= 500, bg='#ffc8dd', height= 100,
                bd=0, highlightthickness=0, relief= 'ridge')
margin.pack()
text_id = Label(root, bg='#ffc8dd', text='Quer namorar comigo ?',
                fg='#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#ffb3c1', command=denied,
                     relief=RIDGE, bd=3, font=('Monstserrat', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)
button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=RIDGE,
                     bd=3, command=accepted, font=('Monstserrat', 14, 'bold'))
button_2.pack()

root.mainloop()




'''import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # Importe a classe PhotoImage da biblioteca PIL
import random
from tkinter import messagebox

root = tk.Tk()
root.title('Aceita ?')
root.geometry('600x600')

# Carregue a imagem de plano de fundo usando o PhotoImage
background_image = Image.open("background_image.png")
background_photo = ImageTk.PhotoImage(background_image)

# Crie um widget de etiqueta para exibir a imagem de plano de fundo
background_label = Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)  # Preencha todo o espaço do widget raiz

# Restante do seu código...

root.mainloop()
'''