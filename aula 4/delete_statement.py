import mysql.connector

conexao = mysql.connector.connect(user='root',
                                     password='lui1234',
                                     host='127.0.0.1',
                                     database='db_locadora')

print('Conexao:', conexao)
cursor = conexao.cursor()

sql = '''DELETE FROM tb_carro WHERE nome = 'mazda'; '''

cursor.execute(sql)


cursor.close()
conexao.close()

print("Operação concluida")