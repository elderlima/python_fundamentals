from sqlalchemy import delete
from core import user_table, engine

con = engine.connect()

nome = input('Digite o nome do usario que sera deletado: ')

apaga = delete(user_table).where(user_table.c.nome == nome)

resultado = con.execute(apaga)
print(resultado.rowcount)