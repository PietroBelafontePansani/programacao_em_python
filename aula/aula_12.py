# def comparar_par_ou_impar():
#     n1 = int(input('digiti um numero'))
#     n2 = int(input('digiti um numero'))

#     if n1 % 2 == 0 and n2 % 2 == 0:
#         print(f' ambos são par')
#     elif n1 % 2 == 0 or n2 % 2 == 0:
#         print(f'{n1,n2} um deles é par')
#     else:
#         print('nem um é par')    
# comparar_par_ou_impar()

# def mult():
#     n = 5
#     b = 2
#     x = 2
#     mult = n * b * x
#     print(mult)
# mult()

# def elevado():
#     n1 = 23
#     n2 = 2
#     elevado = n1 ** n2
#     print(elevado)
# elevado() 

def usuario():
    n1 = int(input('digiti um numero: '))
    if n1 <18:
        print('não tem mensagem')
    else:
        print('você é legal')    
    n1 = 18
usuario()    