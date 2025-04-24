import mysql.connector

conexao_db = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='localhost',
                                     database='db_loja_2')

print('Conexao:\n', conexao_db)

cursor_db = conexao_db.cursor()
sql = ''' CREATE TABLE IF NOT EXISTS tb_produto(
        idt INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(45) NOT NULL UNIQUE,
        preco DECIMAL(9,2) NOT NULL,
        data_validade DATE NULL,
        PRIMARY KEY (idt)
)'''
cursor_db.execute(sql)

cursor_db.close()
conexao_db.close()

print("conexão fechada")