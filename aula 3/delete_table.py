import mysql.connector

conexao = mysql.connector.connect(user='root',
                                     password='lui1234',
                                     host='127.0.0.1',
                                     database='db_icami')

print('Conexao:', conexao)
cursor = conexao.cursor()

sql = '''DROP TABLE tb_gerente'''

cursor.execute(sql)


cursor.close()
conexao.close()

print("Operação concluida")