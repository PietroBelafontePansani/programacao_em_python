import tkinter as tk



janela = tk.Tk()
janela.geometry('1400x1024')
janela.configure(bg = 'black')


texto = tk.Label(janela, text = 'NOME', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)

texto = tk.Label(janela, text = 'IDADE', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)

texto = tk.Label(janela, text = 'E-MAIL', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)

texto = tk.Label(janela, text = 'ENDEREÇO', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)

texto = tk.Label(janela, text = 'CELULAR', font=('arial',15), fg = 'white', bg = 'black')
texto.pack(pady = 20)

input_ = tk.Entry(janela, font = ('arial',25), bg = 'white', fg = 'black')
input_.pack(padx = 15)

texto = tk.Label(janela, text = 'SEU TEXTO AQUI', font=('arial',25), fg = 'white', bg = 'black')
texto.pack

janela.mainloop()