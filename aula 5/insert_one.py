import mysql.connector

conexao = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='localhost',
                                     database='db_loja_2')

print('Conexao:', conexao)

cursor = conexao.cursor()

v_nome = input("Nome: ")
v_preco = input("Preço: ")
v_data = input("Data (AAAA-MM-DD): ")

sql = f'''INSERT INTO tb_produto (nome, preco, data_validade)
         values('{v_nome}', {v_preco}, '{v_data}')'''


cursor.execute(sql)
conexao.commit()

cursor.close()
conexao.close()

print("Operação concluida")