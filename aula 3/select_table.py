import mysql.connector

conexao = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='127.0.0.1',
                                     database='db_empresa')

print('Conexao:', conexao)
cursor = conexao.cursor()

sql = '''SELECT * from tb_funcionario'''

cursor.execute(sql)
funcionario = cursor.fetchall()

print(funcionario)

for func in funcionario:
    print(func)

for func in funcionario:
    print("ID:", func[0])
    print("Nome:", func[1])
    print("Salario:", func[2])
