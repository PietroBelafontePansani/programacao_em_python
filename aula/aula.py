def soma():
    n1 = int(input('nº: '))
    n2 = int(input('nº: '))
    print(n1+n2)

def sub():
    n1 = int(input('nº: '))
    n2 = int(input('nº: '))
    print(n1-n2)

def mult():
    n1 = int(input('nº: '))
    n2 = int(input('nº: '))
    print(n1*n2)

def div():
    n1 = int(input('nº: '))
    n2 = int(input('nº: '))
    print(n1/n2)

def calculadora():
    print('calculadora z')
    operacao = input('''
                     Escolha a operação
                     (+) - (-) - (*) - (/)
                     ''')
    if operacao == '+':
        soma()
    elif operacao == '-':
        sub()
    elif operacao == '*':
        mult()
    elif operacao == '/':
        div()
    else:
        print('digiti algo valido')


calculadora()            

