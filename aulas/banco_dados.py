#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

# import psycopg2

# def insert_in_table(nome, conteudo):
#     try:
#         con = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
        
#         cur = con.cursor()
#         cur.execute(f"insert into scripts(nome, conteudo) values ('{nome}', '{conteudo}')")
#         # cur.execute("select * from scripts")
#         con.commit()
#         # print(f'O Primeiro registro é {cur.fetchone()}')
#         # print(f'Todos os outros registros: {cur.fetchall()}')
#         print("Sucesso")

#     except Exception as e:
#         print(f'Erro: {e}')
#         print('Fazendo rollback')
#         con.rollback()

#     finally:
#         print('Finalizando conexao com o banco de dados')
#         cur.close()
#         con.close()


# insert_in_table('elder', 'santos')

from pymongo import MongoClient

client = MongoClient('localhost')
db = client['dexterops']

def insert_dados():
    db.fila.insert({
        "_id":10, 
        "empresa":"4linux", 
        "cursos": [
                        {
                            "nome":"InfraAgil",
                            "carga horaria":40
                        },
                        {
                            "nome":"Continuos monitoring",
                            "carga horaria":40
                        }
                   ]
        })

# insert_dados()

def select_dados():
    for r in db.fila.find():
        print(f"Empresa: {r['empresa']}")
        for c in r['cursos']:
            print('===============')
            print(f"Nome: {c['nome']} \nCarga Horaria: {c['carga horaria']}\n")

select_dados()