import mysql.connector

conexao = mysql.connector.connect(user='root',
                                     password='lui1234',
                                     host='127.0.0.1',
                                     database='db_icami')

print('Conexao:', conexao)

cursor = conexao.cursor()

sql = '''INSERT INTO tb_gerente
         values(1231, "Jonas", 1500.50, 45, "Onde o cascao toma banho / socorro-sp")'''

cursor.execute(sql)
conexao.commit()

cursor.close()
conexao.close()

print("Operação concluida")