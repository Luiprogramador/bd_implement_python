#1. Desenvolva um programa em Python para criar uma base de dados com o SQLite e uma tabela com uma chave primária, pelo menos duas colunas obrigatória e pelo menos duas colunas opcionais. 


import sqlite3

database = "loja.db"
conexao = sqlite3.connect(database)

cursor = conexao.cursor()

sql = '''CREATE TABLE IF NOT EXISTS db_vendedor(
cpf text PRIMARY KEY,
nome  text not null,
endereco text not null,
idade integer,
data_nasc integer)'''

cursor.execute(sql)
conexao.commit()
cursor.close()
conexao.close()

print("Banco de dados fechado")