import sqlite3

database = "livraria.db"
conexao = sqlite3.connect(database)

cursor = conexao.cursor()

sql = '''select * from db_client'''

cursor.execute(sql)
l_registros = cursor.fetchall()
for regis in l_registros:
    print(regis)