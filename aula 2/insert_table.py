#2. Implemente um programa em Python para inserir dados na tabela criada. Insira pelo menos quatro registros na tabela

import sqlite3

database = "loja.db"
conexao = sqlite3.connect(database)

cursor = conexao.cursor()

sql = '''insert into db_vendedor
    values('43264534673', 'umpa lumpa', 'guará', 10, 2015)'''


cursor.execute(sql)
conexao.commit()
cursor.close()
conexao.close()