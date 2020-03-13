# #!/usr/bin/python3

# """
# 09/02/2020
# """

# #1o - Exercicio
# # Faça um script que peça o seu nome e imprima a seguinte saudação: Olá, meu nome é <seu nome>

# # nome = input("Qual o seu nome?\n")
# # print("Olá, meu nome é %s" % nome)

# #2o - Exercicio
# #Dado a lista
# # times = [["Gamba", "Peppa", "Bambi"], ["Preto", "Branco", "Verde", "Vermelho"]]

# # #Imprima na tela as seguintes mensagens
# # #time; <nome_time>, cores: <cores_time>

# # print("Time:", times[0][0], "- Cores:", times[1][0], times[1][1])
# # print("Time:", times[0][1], "- Cores:", times[1][2], times[1][1])
# # print("Time:", times[0][2], "- Cores:", times[1][3], times[1][1], times[1][0])

# #3o - Exercicio
# #Dado os Dados;
# dados = {"estados":{
#                     "sp": {
#                             "nome": "Sao Paulo", 
#                             "Municipios": 645, 
#                             "População": 44.04
#                             },
#                     "rj": {
#                             "nome": "Rio de Janeiro", 
#                             "Municipios": 92, 
#                             "População": 16.72
#                             },
#                     "mg": {
#                             "nome": "Minas Gerais", 
#                             "Municipios": 31, 
#                             "População": 20.87
#                             }
#                     }
#         }

# #Imprima na tela as seguintes mensagens:
# #
# #Estado: <nome_estado>
# #Municipios: <qnt_municipios>
# #População: <qnt_população>

# # print("Estado:", dados["estados"]["sp"]["nome"], "\nMunicipios:", dados["estados"]["sp"]["Municipios"], "\nPopulação:", dados["estados"]["sp"]["População"])
# # print("\nEstado:", dados["estados"]["rj"]["nome"], "\nMunicipios:", dados["estados"]["rj"]["Municipios"], "\nPopulação:", dados["estados"]["rj"]["População"])
# # print("\nEstado:", dados["estados"]["mg"]["nome"], "\nMunicipios:", dados["estados"]["mg"]["Municipios"], "\nPopulação:", dados["estados"]["mg"]["População"])

# # for estados in dados["estados"].key():

# #n1 += 10 é o mesmo que 10 = n1 + 10

# # idade = int(input("Digite sua idade: "))

# # if idade >= 18:
# #     print("Você é maior de idade")
# # else:
# #     print("Você é menor de idade")

# #####
# # # 4o - Exercicio
# # s1 = int(input("Digite a nota dp 1o Semestre: "))
# # s2 = int(input("Digite a nota dp 2o Semestre: "))
# # s3 = int(input("Digite a nota dp 3o Semestre: "))
# # s4 = int(input("Digite a nota dp 4o Semestre: "))

# # media = (s1 + s2 + s3 + s4)/4

# # print("\nA media do aluno é ", media)

# # if media >= 7:
# #     print("\nAluno aprovado!")
# # elif media >= 5 and media <= 7:
# #     print("\nAluno em Recuperação!")
# # else:
# #     print("\nAluno reprovado!")

# #5o Exercicio

# # var1 = int(input("Digite o 1o valor: "))
# # var2 = int(input("Digite o 2o valor: "))

# # if var1 == var2:
# #     print("é igual que ")
# # elif var1 >= var2:
# #     print("é maior que ")
# # else:
# #     print("é menor que ")

# """
# Software de folha de pagamento

# Programa para o cálculo de uma folha de pagamento, Os descontos são do Imposto de Renda, que
# depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
# 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).

# O Salário Líquido corresponde ao Salário Bruto menos os descontos.

# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:

# Salário Bruto       Desconto IR
# Até 1.900           isento
# De 1.901 até 2.800  7%
# De 2.801 até 3.700  15%
# de 3.701 até 4.600  22%
# Acima de 4.600  27%

# Imprima na tela as informações, dispostas conforme o exemplo abaixo.

# Valor da hora:  6.0
# Quantidade de horas trabaçhadas:  220.0
# Salario Bruto:  R$ 1320.0
# (-) IR: R$ 0
# (-) Sindicato: R$ 39.6
# FGTS (11%): R$ 145.2
# Total de Desconto:  R$ 39.6
# Salario Liquido: R$ 1280.4

# """

# # hora = float(input("Digite o valor da sua hora: "))
# # trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
# # bruto = (hora * trabalhadas)

# # if bruto > 4600:
# #     ir = 27
# # elif bruto <= 4600 and bruto >= 3701:
# #     ir = 22
# # elif bruto <= 3700 and bruto >= 2801:
# #     ir = 15
# # elif bruto <= 2800 and bruto >= 1901:
# #     ir = 7
# # else:
# #     ir = 0

# # calc_ir = bruto*(ir / 100)
# # sindicato = (bruto*3)/100
# # fgts = (bruto*11)/100

# # desconto = (ir + sindicato)

# # liquido = (bruto - desconto)

# # print(f"Valor da hora: {hora}")
# # print("\nQuantidade de horas trabaçhadas: ", trabalhadas)
# # print("\nSalario Bruto: ", bruto)
# # print("\n(-) IR: ", ir)
# # print("\n(-) Sindicato: ", sindicato)
# # print("\nFGTS (11%): ", fgts)
# # print("\nTotal de Desconto: ", desconto)
# # print("\nSalario Liquido: ", liquido)

# """
# A partir do ID do produto mostrarmos o nome e o preço
# Caso o nome nao exista, mostraremos a seguinte mensagem
# Produtos inexistente
# """

# try:
#     produtos = dict(produtos=dict(
#                                 p1=dict(nome="Camiseta Star Wars", preco=99.90), 
#                                 p2=dict(nome='Caneca Ricky&Morty', preco=49.90), 
#                                 p3=dict(nome='Camiseta SpiderMan', preco=69.90)
#                             )
#                 )
# # """
# # Printar todos os valores:
# # print(produtos)

# # Printar só o nome e o preço
# # print("Nome:", produtos["produtos"]["p1"]["nome"], "- Preço:", produtos["produtos"]["p1"]["preco"])

# # print("Keys dentro de produtos: ", produtos["produtos"].keys())
# # print("Keys dentro de p1: ", produtos["produtos"]["p1"].keys())
# # """

# #     x = input("Digite o ID do produto ")

# #     if x not in produtos["produtos"]:
# #         raise ValueError("Produtos inexistente")
# #         #print("Falha")
# #     else:
# #         print("Nome:", produtos["produtos"][x]["nome"], "- Preço:", produtos["produtos"][x]["preco"])

# # except ValueError as e:
# #     print(e)

# # 
# # Crie uma classe mamifero com os atributos:
# #         bebe leite

# # Crie uma classe como sapiens com atributos:
# #         Caça - True
# #         polegares = True
# #         formaCaminhar = 'bipede'

# # Metodos:
# #         Caçar
# #         Comer
# #         Dormir
# #         Construir
# # 

class Mamifero():

        def __init__(self):
                self.bebe_leite = True

class HomoSapiens(Mamifero):

        def __init__(self):
                Mamifero.__init__(self)
                self.caçar = True
                self.polegares = True
                self.formaCaminhar = 'bipede'

        def cacar(self):
                print('Caçando')

        def comer(self):
                print('Comendo')

        def dormir(self):
                print('Dormindo')

        def construir(self):
                print('Construindo')

humano = HomoSapiens()
print(humano.bebe_leite)
humano.construir()

class Personagem():
        
        def __init__(self, nome):
                self.nome = nome
                self.hp = 100
                self.xp = 0
                self.
                self.

        def __init__(self):
                self.
                self.
                self.
                self.
                self.