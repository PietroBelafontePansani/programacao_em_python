import tkinter as tk
import customtkinter

def display():
    text_capturado = input_.get()
    texto.config(text= text_capturado)










janela = tk.Tk()
janela.geometry('1400x1024')
janela.configure(bg = 'black')

texto = tk.Label(janela, text = 'SISTEMA PARA SALVAR TEXTO', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)



input_ = tk.Entry(janela, font = ('arial',25), bg = 'white', fg = 'black')
input_.pack(padx = 15)

texto = tk.Label(janela, text = 'SEU TEXTO AQUI', font=('arial',25), fg = 'white', bg = 'black')
texto.pack(pady = 30)



btn = customtkinter.CTkButton(janela,text = 'salvar texto', fg_color = 'red', corner_radius = 25, command=display)
btn.pack()



janela.mainloop()