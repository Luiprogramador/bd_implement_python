import mysql.connector

conexao_db = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='127.0.0.1')
                                     # database='')

print('Conexao:\n', conexao_db)

cursor_db = conexao_db.cursor()
sql = "CREATE DATABASE IF NOT EXISTS db_empresa"
cursor_db.execute(sql)

cursor_db.close()
conexao_db.close()

print("Conexao fechada")