# numero = int(input('Digite um número: '))


# def par_impar():
#     '''Utilizando variáveis globais -  fora da função'''
#     if  numero % 2 ==  0:
#            print('O número é par!')
#     else:    
#            print('é impar') 
# par_impar()           



# def mult_3():
#     ''' Variáveis locais'''
#     n1  =  int(input('Digite um número: '))
#     n2  =  int(input('Digite um número: '))
#     n3  =  int(input('Digite um número: '))
#     m = n1 * n2 * n3
#     print('Resultado:',m)


# mult_3()    



# def valor_ele(numero, elevado):
    #   ''' Utilizando parâmetro'''
#     print(numero** elevado)



# valor_ele(10,2)




# def descobre_idade(ano_tual, ano_nasc,mes):
#     idade  =  ano_tual - ano_nasc
#     if mes >=10:
#         print(idade-1)
#     else:
#         print(idade)


# descobre_idade(2025,2000,2)


# def bra_():
#     copas_brs = [1958,1962,1970,1994,2002]
#     ano = int(input('Ano -> '))
#     if ano in copas_brs:
#         print('Esse ano o brasil ganhou')
#     else:
#         print('Esse ano o Brasil não ganahou ')


# bra_()            



# def cumprimentar():
#     print('Sejam bem vindo!')



# def restaurante():
#     cumprimentar()
#     i = input('Deseja fazer o pedido: ')
#     prods = []
#     while i == 'sim':
          
#           produto =  input('''Digite o nome do produto:
#                            SALADA 
#                            MACARRONADA
#                            SORVETE
#                            SANDUIIXCHE''')
#           prods.append(produto)
#           print(prods)
#           i = input('Deseja CoNTINUAR: ')


# restaurante()

# import meu_modulo as mb


# def mercado():
#     nome  =  input('Nome:')
#     lista = ['','arroz','feijão','frango']
#     valores = [0,15.0,9.50,10.0]
#     carrinho = []
#     me_total = []
#     ped = input('Deseja pedir? ')
#     while ped == 'sim':
#         id  = int(input('Id do produto 1 - 2 -3'))
#         carrinho.append(lista[id])
#         me_total.append(valores[id])
#         print('PRODUTOS NO CARRINHO:')
#         print(carrinho)


#         print('Total - R$ ', sum(me_total))
#         ped = input('Deseja continuar? ')
        
#     else:
#         escolha  =  int(input(' FORMA DE PAGAMENTO - 1 - px 2 - cc  3 - cd'))    
#         var = mb.pag(escolha)
#         des = mb.despedir(nome)


# mercado()


