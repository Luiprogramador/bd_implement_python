import mysql.connector

conexao = mysql.connector.connect(user='root',
                                     password='lui1234',
                                     host='127.0.0.1',
                                     database='db_icami')

print('Conexao:', conexao)
cursor = conexao.cursor()

sql = '''SELECT * from tb_gerente'''

cursor.execute(sql)
gerente = cursor.fetchall()

if not gerente:
    print("tabela vazia.")

else:
    for func in gerente:
        print(func)

    for func in gerente:
        print("ID:", func[0])
        print("Nome:", func[1])
        print("Salario:", func[2])
        print("Idade:", func[3])
        print("Endereço:", func[4])


cursor.close()
conexao.close()

print("Operação concluida")