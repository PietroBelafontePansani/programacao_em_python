#**Exercício 0:** Escreva um programa que use a função
#`range()` para gerar os números pares de 2 a 20 e, em
#seguida, imprima cada número.


print(list(range(2,21)))


#**Exercício 1:** Crie uma lista chamada numeros que
#contenha os números inteiros de 1 a 10 e imprima-a na tela.

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

#*Exercício 2:** Acesse e imprima o terceiro elemento da
#lista `numeros`.

terceiro = numeros[2]
print(terceiro)


#Exercício 3:** Adicione o número 9 à lista `numeros` e
#imprima a lista atualizada.

numeros.append(9)
print(numeros)



#**Exercício 4:** Remova o número 5 da lista `numeros` e
#imprima a lista resultante.

numeros.remove(5)
print(numeros)

#**Exercício 5:** Crie uma lista chamada carros contendo
#três nomes de carros diferentes. Em seguida, concatene
#essa lista com a lista `numeros` e imprima o resultado.

carros = ['ferrari','jeep','mustang']
print(carros, numeros)

carros.extend(numeros)
print(carros)

dicionario = {
'chave':'valor',
'chave':'valor',
}

produtos = ['livros','tablets','fones']

produtos = {'livros':{30.00},
            'tablets':{900.00},
            'fones':{65.00},

            'carrinho':{'livros','tablets','fones'},
            'forma_de_pagamento':{'cd','cc','pix'}
            

            
            
            
            }
print(produtos)

# Crie um e-commerce com a estrutura de dicionários.


# Produtos:  Livros, tablets e fones de ouvido


e_commerce ={


'Livros':{
   'a':20.0,
   'b':30.0,
   'c':40},
'tables':{
'samsumng':100.0,
'motorola':1000.0,
},
'fones':{
'a':50,
'b':60
}   
}



e_commerce2={


'table':20,
'fone':10,
'livro':100



}



e_commerce3 = {


'fone':['a','b','c'],
'valore_fones':[10,20,30],
'tablets':['a','b','c'],
'livro':['a','b','c'],
'cpf':(123,456,78),
'teste':{10,20,30}
}
