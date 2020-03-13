#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String, DateTime)

from datetime import datetime

engine = create_engine('sqlite:///banco.db', echo=True)

metada = MetaData(bind=engine)

user_table = Table('usuarios',
                    metada,
                        Column('id', Integer, primary_key=True),
                        Column('nome', String, index=True),
                        Column('idade', Integer, nullable=False),
                        Column('senha', String),
                        Column('criado em', DateTime, default=datetime.now),
                        Column('atualizado em', DateTime, onupdate=datetime.now)
                    )

metada.create_all(engine)