#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# NUMEROS PRIMOS
#
# def primo(x):
#     y = 1
#     count1 = 0
#     count2 = 0
     
#     # for y in range(x):
#     while y <= x:
#         var1 = x / y and x % y == 0
#         if var1 is True:
#             count1 += 1
#             # count1.append(y)
#         else:
#             count2 += 1
#             # count2.append(y)
#         y += 1
    
#     if count1 == 2:
#         print(f'\nO numero {x} é primo')
#     else:
#         print(f'\nO numero {x} não é primo')

# numero = int(input("Digite um numero inteiro: "))
# primo(numero)

# AREA
#
# x = int(input('Digite 1o numero: '))
# y = int(input('Digite 2o numero: '))

# hipo = x**2 + y**2

# print(hipo)

#
# FIBONACCI
#
# x = 0
# y = 1
# z = 0
# num = int(input('Digite um numero: '))

# while z <= num:
#     z = x + y
#     print(z)
#     x = y
#     y = z
# if z == num:
#     print(f'O numero {num} é Fibonacci')
# else:
#     print(f'O numero {num} não é Fibonacci')
#
#CALCULAR MEDIA

# numero = 0
# soma = 0
# media = 0
# count = 1
# resulta = 0

# while count == 1:
#     media += 1
#     numero = float(input('Digite um numero inteiro:\
#         \n>>> '))
#     if numero == 0:
#         print('Digite um valor maior que 0!')
#     else:
#         soma += numero
#     resultado = soma / media
#     print('Soma total: ', soma)
#     print('Media: ', resultado)
#     count = int(input('Continuar?\
#         \n\nDigite 1 para Sim\
#         \nDigite 2 para Nao\
#         \n>>> '))

# num = int(input('Digite um numero: '))

x = 1

while x <= 10:
    for y in range(1, 11):
        calc = x * y
        print(f'{x} x {y} = {calc}')
    print('\n')
    x += 1


    # x += 5
    # if x % 2 == 0:
    #     print(f"{x} é par")
    # else:
    #     print(f"{x} é impar")