import mysql.connector

conexao = mysql.connector.connect(user='root',
                                     password='lui1234',
                                     host='127.0.0.1',
                                     database='db_locadora')

print('Conexao:', conexao)

cursor = conexao.cursor()

sql = '''INSERT INTO tb_carro (nome, marca, ano, qnt_estoque, qnt_km)
         values("civic", "honda", "2025-04-07", 5, 0)'''

sql1 = '''INSERT INTO tb_carro (nome, marca, ano, qnt_estoque, qnt_km)
         values("gol", "wolksvagen", "2010-03-04", 10, 200),
         ("veracruz", "hyundai", "2015-04-20", 1, 100.3),
         ("qq", "cherry", "2022-04-20", 4, 50.0),
         ("duster", "Renault", "2017-03-12", 2, 6.0),
         ("miata", "mazda", "1990-04-03", 1, 400)'''

cursor.execute(sql)
cursor.execute(sql1)
conexao.commit()

cursor.close()
conexao.close()

print("Operação concluida")