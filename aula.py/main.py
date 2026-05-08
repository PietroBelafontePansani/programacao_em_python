print(' Scrum Master é um líder servidor que ajuda a equipe a seguir os princípios e práticas do Scrum')
print('_________________________________________________________________________________________________')
print('importância garantir que a equipe siga os princípios e práticas do Scrum, agindo como um líder servidor que remove impedimentos,' \
' facilita a comunicação e a colaboração e promove a melhoria contínua do processo')
print('____________________________________________________________________________________________________________________________________')
print('"PO" pode significar tanto Product Owner quanto Purchase Order (ordem de compra), dependendo do contexto')
print('__________________________________________________________________________________________________________')
print('importância pode se referir a Product Owner, um papel-chave em metodologias ágeis para maximizar o valor do produto; à Pesquisa Operacional,' \
' uma ferramenta para otimizar decisões e recursos em cenários complexos; ou a Procedimentos Operacionais, que padronizam rotinas para aumentar produtividade e qualidade')
print('_________________________________________________________________________________________________________________________________________________________________________')
print('líder de equipe de TI é um profissional que combina expertise técnica com habilidades de gestão para guiar uma equipe na entrega de projetos e soluções tecnológicas')
print('______________________________________________________________________________________________________________________________________________________________________')
print('importância ele alinha a tecnologia aos objetivos de negócio, gerencia equipes, otimiza infraestruturas, garante a segurança da informação e impulsiona a inovação')
print('____________________________________________________________________________________________________________________________________________________________________')
print('equipe de tecnologia é um conjunto de profissionais responsáveis por gerenciar a infraestrutura e as soluções tecnológicas de uma organização, o que inclui o suporte técnico,' \
' o desenvolvimento de software e a segurança de dados')
print('________________________________________________________________________________________________________________________________________________________________________________')
print('importância garantir que os sistemas de TI estejam funcionando perfeitamente, desenvolver e implementar soluções personalizadas, proteger dados e dar suporte aos usuários,' \
' além de agir como parceira estratégica para alinhar a tecnologia aos objetivos de negócio')
print('____________________________________________________________________________________________________________________________________________________________________________________')

#-----------------------------------------------------------------------
# pro codding -> codifica

import streamlit as st
import pandas as pd


st.title('teste')
dados = pd.read_csv('vendas.csv')

df = pd.DataFrame(dados)
st.bar_chart(df, x = 'nome', y = 'venda')

#-----------------------------------------------------

st.caption('Paragrafo')
st.audio('audio.mp3')
st.image('img.jpg', width=250)

#-----------------------------------------------------

# calculadora

st.title('calculadora')

st.caption('colocar 1 depois outro numero escolha a operação e ver o resultado')

n1 = st.number_input('primero numero')
n2 = st.number_input('segundo numero')

escolha = st.selectbox('escolha a operação: ',['+','-','*','/'])

if st.button('calcular'):
    if escolha == '+':
        soma = n1 + n2
        resultado = soma
    elif escolha == '-':
        sub = n1 - n2
        resultado = sub
    elif escolha == '*':
        mult = n1 * n2
        resultado = mult
    elif escolha == '/':
        div = n1 / n2
        resultado = div

    st.success(resultado)

#----------------------------------------------------------------     
import streamlit as st

st.title('calcular imc')

n1 = st.number_input('peso:')
n2 = st.number_input('altura:', value = 0.1)

imc = n1/(n2**2)

if st.button('calcular imc'):
    if imc:
        st.success(imc)
#----------------------------------------------------------------

st.caption('CADASTRO SIMPLES')

nome = st.text_input('Nome: ')
idade = st.number_input('Idade: ')
email = st.text_input('email: ')
altura = st.number_input('Altura: ')

if st.button('Cadsatrar'):
    st.success('Pessoa cadsatrada')
#---------------------------------------------------------------

