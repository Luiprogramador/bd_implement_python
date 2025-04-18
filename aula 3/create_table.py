import mysql.connector
import os

os.system("cls")

conexao = mysql.connector.connect(user='root',
                                     password='lui1234',
                                     host='127.0.0.1',
                                     database='db_icami')

print('Conexao:', conexao)
cursor = conexao.cursor()
sql = '''CREATE TABLE IF NOT EXISTS tb_gerente(
         idt INT AUTO_INCREMENT,
         nome VARCHAR(45) NOT NULL,
         salario DECIMAL(9,2) NULL,
         idade INT NULL,
         endereco VARCHAR(50) NOT NULL,
         PRIMARY KEY (idt)
         )'''
cursor.execute(sql)
cursor.close()
conexao.close()
print("Conexão fechada")



