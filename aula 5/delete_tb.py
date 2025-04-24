import mysql.connector

conexao = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='localhost',
                                     database='db_loja_2')

print('Conexao:', conexao)
cursor = conexao.cursor()

sql = '''DROP TABLE tb_produto'''

cursor.execute(sql)


cursor.close()
conexao.close()

print("Operação concluida")