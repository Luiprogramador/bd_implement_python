#2. Implemente um programa em Python para inserir dados na tabela criada. Insira pelo menos quatro registros na tabela

import sqlite3

database = "loja.db"
conexao = sqlite3.connect(database)

cursor = conexao.cursor()

sql = '''insert into db_vendedor
    values('432645346343', 'Ray ano', 'Vicente pires', 22, 2003)'''


cursor.execute(sql)
conexao.commit()
cursor.close()
conexao.close()