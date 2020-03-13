from core import engine, user_table

con = engine.connect()
insert = user_table.insert()

new = insert.values(idade=25, nome='Caio', senha='abacaxi123')

con.execute(user_table.insert(),[
    # {'nome':'fulano', 'idade':20, 'senha': 'limão'},
    # {'nome':'beltrano', 'idade':18, 'senha': 'limão123'},
    {'nome':'ze das coves', 'idade':20, 'senha': 'limãoazedo'}
])