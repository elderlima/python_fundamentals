#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# class classe(): #Declarando a Classe. O ":" indica vamos iniciar o bloco
#     def __init__(self): #O __init__ é o Construtor. Será chamdo sempre que criarmos objetos da classe "classe"
#         self.atributo1 = '1o Atributo'
#         self.atributo2 = '2o Atributo'
#         self.atributo3 = '3o Atributo'
#         self.atributo4 = '4o Atributo'
#         self.atributo5 = '5o Atributo'

#     def metodo1(self):# Metodo é uma função associada a uma classe
#         self.atributo6 = '1o Atributo do 1o Metodo'
#         self.atributo7 = '2o Atributo do 1o Metodo'
#         self.atributo8 = '3o Atributo do 1o Metodo'
#         self.atributo9 = '4o Atributo do 1o Metodo'
#         self.atributo10 = '5o Atributo do 1o Metodo'

# objeto = classe()
# objeto.metodo1()
# print(objeto.atributo6)
# print(objeto.atributo1)
# print(objeto.atributo5)

class oldbank():

    def __init__(self):
        self.número_identificador_do_banco = '999'
        self.número_da_conta = '001'
        self.agencia = '08'
        self.nome_do_cliente = 'Fulano Beltrano'
        self.saldo = 1000

    def depositar(self):
        self.valor_deposito = int(input('Digite o valor do Deposito: R$ '))
        if self.valor_deposito > 0:
            self.saldo = self.saldo + self.valor_deposito
            print('Deposito efetuado com sucesso! Seu saldo atual é de: R$', self.saldo)
        else:
            print('Valor invalido! Digite um valor maior que: R$', self.valor_saque)
                
    def sacar(self):
        self.valor_saque = int(input('Digite o valor do Deposito: R$ '))
        if self.saldo < self.valor_saque:
            print('Saque Indisponivel. Digite um valor menor que: R$', self.saldo)
        else:
            self.saldo = self.saldo - self.valor_saque
            print('Saque Efetuadoefetuado com sucesso! Seu saldo atuale é: R$', self.saldo)

        # self.saldo = self.saldo - valor
            
    def extrato(self):
        # print('mostra o número do banco, o número da agência, nome do cliente e o saldo')
        print('Numero do Banco:', self.número_identificador_do_banco)
        print('Agencia:', self.agencia)
        print('Cliente:', self.nome_do_cliente)
        print('Saldo: R$', self.saldo)

def menu():
    print('\nOldBank\
        \nBem vindo(a)!\
        \n\nSelecione a opção abaixo:\
        \nPara extrato digite 1\
        \nPara saque digite 2\
        \nPara deposito digite 3\n')
    
    opcao = int(input('>>> '))
    
    if opcao == 3:
        cliente = oldbank()
        cliente.depositar()
    elif opcao == 2:
        cliente = oldbank()
        cliente.sacar()
    elif opcao == 1:
        cliente = oldbank()
        extrato = cliente.extrato()
    else:
        raise ValueError('Valor Inexistente')
    
menu()