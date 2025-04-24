import mysql.connector

conexao_db = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='localhost')
                                     # database='db_empresa')

print('Conexao:\n', conexao_db)
conexao_db.close()
