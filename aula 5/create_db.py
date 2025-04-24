import mysql.connector

conexao_db = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='localhost')
                                     # database='db_empresa')

print('Conexao:\n', conexao_db)

cursor_db = conexao_db.cursor()
sql = "CREATE DATABASE IF NOT EXISTS db_loja_2"
cursor_db.execute(sql)

cursor_db.close()
conexao_db.close()

print("conexão fechada")