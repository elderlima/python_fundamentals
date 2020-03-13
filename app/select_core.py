from sqlalchemy import select
from core import user_table

#select
# selecione = select([user_table])
# print([x for x in selecione.execute()])

# select com filtro
filtro = input('Digite o nome do usuario: ')

selecione_filtro = select([user_table]).where(user_table.c.nome == filtro)

print([f for f in selecione_filtro.execute()])