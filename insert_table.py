import sqlite3

database = "livraria.db"
conexao = sqlite3.connect(database)

cursor = conexao.cursor()

sql = '''insert into db_client
    values('26423693462', 'Cleudes', 19)'''

cursor.execute(sql)
conexao.commit()
cursor.close()
conexao.close()