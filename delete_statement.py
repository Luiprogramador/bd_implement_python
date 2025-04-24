import mysql.connector

conexao = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='localhost',
                                     database='db_loja_2')

print('Conexao:', conexao)
cursor = conexao.cursor()

nome = input("Nome: ")
sql = f'''DELETE FROM tb_produto WHERE nome = '{nome}'; '''

cursor.execute(sql)


cursor.close()
conexao.commit()
conexao.close()

print("Operação concluida")