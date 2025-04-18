import mysql.connector

conexao_db = mysql.connector.connect(user='root',
                                     password='lui1234',
                                     host='127.0.0.1',
                                     database='db_locadora')

print('Conexao:\n', conexao_db)

cursor_db = conexao_db.cursor()
sql = ''' CREATE TABLE IF NOT EXISTS tb_carro(
        idt INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(45) NOT NULL UNIQUE,
        marca VARCHAR(45) NOT NULL,
        ano DATE NOT NULL,
        qnt_estoque INT NULL,
        qnt_km DECIMAL NULL,
        PRIMARY KEY (idt)
)'''
cursor_db.execute(sql)

cursor_db.close()
conexao_db.close()

print("conexão fechada")