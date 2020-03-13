#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from oldbank import oldbank

def menu():
    cliente = oldbank()
    
    while True:
        print('\nOldBank\
            \nBem vindo(a)!\
            \n\nSelecione a opção abaixo:\
            \n\nPara extrato digite 1\
            \nPara saque digite 2\
            \nPara deposito digite 3')
        
        opcao = int(input('>>> '))
        
        if opcao == 3:
            cliente.depositar()
            continue
        elif opcao == 2:
            cliente.sacar()
            continue
        elif opcao == 1:
            cliente.extrato()
            continue            
        else:
            raise ValueError('Valor Inexistente')

menu()