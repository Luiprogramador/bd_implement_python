#3. Faça um programa em Python para consultar todos os registros inseridos na tabela criada. Mostre os registros na horizontal e depois na vertical. E inclua a mensagem de “Tabela vazia.”

import sqlite3
import os
os.system("cls")
database = "loja.db"
conexao = sqlite3.connect(database)

cursor = conexao.cursor()

sql = '''select * from db_vendedor'''

cursor.execute(sql)
l_registros = cursor.fetchall()
if l_registros:
    for regis in l_registros:
        for item in regis:
            print(item)
else: 
    print("Tabela vazia.")


print("-"* 50)

if l_registros:
    for regis in l_registros:
        print(regis)
else:
    print("Tabela vazia.")
