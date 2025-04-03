import mysql.connector

conexao = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='127.0.0.1',
                                     database='db_empresa')

print('Conexao:', conexao)

cursor = conexao.cursor()

sql = '''insert into tb_funcionario
         values(1231, "Jonas", 1500.50)'''

cursor.execute(sql)
conexao.commit()

cursor.close()
conexao.close()

print("Operação concluida")