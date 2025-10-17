import tkinter as tk
from PIL import Image, ImageTk


def display():
    text_capturado = input_NOME.get()
    print(text_capturado)

    text_capturado = input_IDADE.get()
    print(text_capturado)

    text_capturado = input_E_MAIL.get()
    print(text_capturado)

    text_capturado = input_ENDEREÇO.get()
    print(text_capturado)

    text_capturado = input_CELULAR.get()
    print(text_capturado)



janela = tk.Tk()
janela.geometry('1700x750')
janela.configure(bg = 'black')


texto = tk.Label(janela, text = 'NOME', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)

input_NOME = tk.Entry(janela, font = ('arial',25), bg = 'white', fg = 'black')
input_NOME.pack(padx = 15)

texto = tk.Label(janela, text = 'IDADE', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)

input_IDADE = tk.Entry(janela, font = ('arial',25), bg = 'white', fg = 'black')
input_IDADE.pack(padx = 15)

texto = tk.Label(janela, text = 'E_MAIL', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)

input_E_MAIL = tk.Entry(janela, font = ('arial',25), bg = 'white', fg = 'black')
input_E_MAIL.pack(padx = 15)

texto = tk.Label(janela, text = 'ENDEREÇO', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)

input_ENDEREÇO = tk.Entry(janela, font = ('arial',25), bg = 'white', fg = 'black')
input_ENDEREÇO.pack(padx = 15)

texto = tk.Label(janela, text = 'CELULAR', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)

input_CELULAR = tk.Entry(janela, font = ('arial',25), bg = 'white', fg = 'black')
input_CELULAR.pack(padx = 15)

texto = tk.Label(janela, text = 'SEU TEXTO AQUI', font=('arial',25), fg = 'white', bg = 'black')
texto.pack


btn = tk.Button(janela,text = 'Enviar', command = display )
btn.pack()






janela.mainloop() 