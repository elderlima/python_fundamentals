#!/usr/bin/python3
# -*- coding: utf-8 -*-
from functools import reduce
#Shebang - O sistema tenta executar o arquivo usando um interpretador especificado pelo shebang

"""
DOCSTRING

09/03/2010 - 1a-Aula

"""
# Ctrl+Sapce = Atalho para inserir/remover hashtag

# time = input("Qual o seu time?\n")
# print("Seu time é o %s" % time)
# print(type(time))


#endereco = "Rua Vergueiro, 3057"

"""
Metodos de String

print(endereco.capitalize()))
print(endereco.count(e))
print(endereco.upper())
print(endereco.lower())
print(endereco.split())
print(endereco.replace())

Metodos Booleanos

"""
"""
Convertendo variavel para
int = numeros inteiros
str = string
float = numeros decimais
"""
# n1 = int(input("digite o primeiro numero"))
# n2 = int(input("digite o segundo numero"))

# print(n1 + n2)

#LISTAS

# lista = ["a", "b", "c", 12, 15, "casa", "teste"]

# lista[0] = "13"

# print(lista)

#TUPLAS

# linguagens = "python", "java", "php"

# print(linguagens)
# print(linguagens[0])
# print(linguagens[0].upper())

# n1 = ("a", "b", "c", [10, 20], [30, 40])

# n1[4].append([50,60])

# print(n1)

#DICIONARIO

# carros = {"modelos": {"Fox", "Fusca", "Gol"}, "anos": {2003, 1978, 2002}}

# print(carros["modelos"])
# print(carros["anos"])

# produtos = {"produtos": {"001": {"nome": "Camisa Spider-Man", "preço": 99.90}, "002": {"nome": "Camisa Star Wars", "preço": 79.90}}}

# print(produtos["produtos"]["002"]["preço"])

# produtos["produtos"]["001"]["preço"] = 29.90

# print(produtos["produtos"])

#/10/03/2020 - 2a - Aula

# usuarios = dict(renato='abacaxi123', carlos='fusca123', maria='teste321')

# bloqueados = []
# tentativas = 0

# while True:
#     login = input('Digite o seu usuario: ')
#     if login in usuarios:
#         senha = input('Digite sua senha: ')
#         if senha == usuarios[login]:
#             print('login efetuado!')
#             break
#         elif tentativas < 3:
#             print('Senha Incorreta!')
#             tentativas += 1
#             continue
#         else:
#             print('Usuário bloqueado, contate o administrador')
#             bloqueados.append(login)
#             usuarios.pop(login)
#             break
#     else:
#         print('Usuário não cadastrado')
#         continue

# print(f'usuarios: {usuarios}')
# print(f'usuarios bloqueados: {bloqueados}')

# x = 1

# while x < 10:
#     #print("Numero: {}".format(x))
#     print(f"Numero: {x}")
#     x += 1
#     print("O while acabou !")

# while True:
#     print(f"Número: {x}!")
#     x += 1
#     break

# while True:
#     try:
#         x = int(input("Digite o primeiro numero "))
#         y = int(input("Digite o segundo numero "))
#         print(x + y)
#         break
    
#     # except ValueError:
#     #     print("Digite apenas numeros")
#     #     continue
#     except Exception as e:
#         print(e.with_traceback())

# x = 1111

# while x <= 1115:
#     print(x)
#     x += 1

# try:
#     produto_id = [1111, 1112, 1113, 1114, 1115]
#     id_desejado = int(int"Digite o ID desejado ")
#     if id_desejado not in produto_id:
#         raise ValueError("Produto nao cadastrado")
#     else:
#         print("Produto cadastrado")
# except ValueError as e:
#     print(e)

# with open("novo_arquivo", "w") as f:
#     f.write("Meu primeiro arquivo")

# produtos = ['Camisa', 'Tenis', 'Calça', 'Blusa']

# def cadastrarProduto(produto):
#     return produtos.append(produto)
    
# def listaProdutos():
#     return("Produtos cadastrados: \n", produtos)

# def deletaProduto(produto):
#     if produto in produtos:
#         return produtos.remove(produto)
#     else:
#         print("Produto nao cadastrado")

# cadastrarProduto("Cinto")

# listaProdutos()

# deletaProduto('Cinto')

# listaProdutos()

# frutas = []

# def inserFrutas(*args)
#     #frutas.append(args)
#     for f in args:
#         frutas.append(f)

# inserFrutas('abacaxi', 'laranja', 'limao', 'banana')

# print(frutas)

# camisetas = []

# def inserCamiseta(**kwargs):
#     global camisetas
#     camisetas = kwargs
#     return camisetas

# inserCamiseta(camiseta01='Star Wars', camiseta02='Star Trak')

# print(camisetas)

# dobro = lambda x: x * 2

# print(dobro(10))

#função lambda que receba tres valores e retorne a soma

# soma = lambda x, y, z: x + y + z

# print(soma(10, 10, 10))












# x = 2



# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# # map aplica uma função item por item:
# dobro = list(map(lambda x: x * 2, numeros))
# numeros_par = list(filter(lambda x: x % 2 == 0, numeros))
# numeros_impar = list(filter(lambda x: x % 2 != 0, numeros))
# soma = (
#     reduce(lambda x, y: x + y, dobro) + 
#     reduce(lambda x, y: x + y, numeros) + 
#     reduce(lambda x, y: x + y, numeros_par) +
#     reduce(lambda x, y: x + y, numeros_impar)
#     )

# print(dobro)
# print(numeros_par)
# print(numeros_impar)
# print(soma)

#3o - Dia

# from datetime import date

# # random Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
#         return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)

#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))

# class Man(Person):
#     sex = 'Male'

# # man = Man.fromBirthYear('John', 1985)
# # print(isinstance(man, Man))

# # man1 = Man.fromFathersAge('John', 1965, 20)
# # print(isinstance(man1, Man))

# man = Person("Elder", "32")
# print(man.name)
# print(man.age)

#4o Dia

volante = None
motor = None
portas = None

class carro():
    def __init__(self)
        menu() #Estou chamando Menu na linhaX
        self.rodas = 4
        self.volante = menu.volante
        self.motor = menu.motor
        self.portas = menu.portas

    # def __str__(self):
    #     self.confCarros = {'\nConfiguração: ':
    #                     {
    #                     '\nVolante': volante,
    #                     '\nMotor': motor,
    #                     '\nPortas': portas
    #                     }
    #                 }
    
    def ligar(self):
        print('Carro ligado')

    def desligar(self):
        print('Carro desligado')

    def acelerar(self):
        print('Acelerando carro')

    def frear(self):
        print('Freando carro')

def menu():
    volantes = ['volante normal' 'volante redondo']
    motores = ['v8', '1.0', '1.6', '2.0']
    print('Bem vindo ao "Monte seu Carro"')
    print('\nEscolha seu volante\
        \t1- Volante Normal\
        \t2- Volante Esportivo\n')
    volante = int(input('>>> '))
    try:
        if volante ==1:
            volante = volante[0]
        elif volante == 2:
            volante = volante[1]
        else:
            raise ValueError('Valor Inexistente')
    except ValueError as v:
        print(v)
    print(f'Voloante selecionado: {volante}')
    
    print('\nEscolha o Motor:\
        \t1- v8\
        \t2- 1.0\
        \t3- 1.6\
        \t4 - 2.0')
    motor = input(input('>>> '))
    try:    
        if motor ==1:
            motor = motor[0]
        elif motor == 2:
            motor = motor[1]
        elif motor == 3:
            motor = motor[2]
        elif motor == 4:
            motor = motor[3]
        else:
            raise ValueError('Valor Inexistente')
    except ValueError as v:
        print(v)
    print(f'Motor selecionado: {motor}')

    portas = int(input('\nDigite a quantidade de portas: '))
    try:    
        if portas <= 4:
            print(f'Quantidade de portas {portas}')
        else:
            raise ValueError('Valor Inexistente')
    except ValueError as v:
        print(v)
    
    confCarros = {'\nConfiguração: ':
                    {
                    '\nVolante': volante,
                    '\nMotor': motor,
                    '\nPortas': portas
                    }
                }