import mysql.connector

conexao_db = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='127.0.0.1')
                                     # database='db_empresa')

print('Conexao:\n', conexao_db)
conexao_db.close()
