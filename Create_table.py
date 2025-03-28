import sqlite3

database = "livraria.db"
conexao = sqlite3.connect(database)

cursor = conexao.cursor()

sql = '''CREATE TABLE IF NOT EXISTS db_client(
cpf text PRIMARY KEY,
nome  text not null,
idade integer)'''

cursor.execute(sql)
cursor.close()
conexao.close()

print("Banco de dados fechado")