import mysql.connector
from mysql.connector import Error
import os

def conectar_banco():
    try:
        conn = mysql.connector.connect(
            user='root',
            password='ceub123456',
            host='localhost',
            database='db_loja_2'
        )
        return conn
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def consultar_carros_filtro(conn):
    print("\nOpções de filtro:")
    print("1 - Filtrar por nome")
    print("2 - Filtrar por marca")
    print("3 - Filtrar por ano")
    print("4 - Mostrar todos os carros")
    
    opcao = input("\nEscolha uma opção de filtro (1-4): ")
    
    try:
        cursor = conn.cursor(dictionary=True)
        
        if opcao == '1':
            valor = input("Digite o nome (ou parte) do produto: ")
            cursor.execute("SELECT * FROM tb_produto WHERE nome LIKE %s", (f'%{valor}%',))
        elif opcao == '2':
            valor = input("Digite o preço do produto: ")
            cursor.execute("SELECT * FROM tb_produto WHERE marca LIKE %s", (f'%{valor}%',))
        elif opcao == '3':
            valor = input("Digite a data de validade (AAAA-MM-DD): ")
            cursor.execute("SELECT * FROM tb_produto WHERE ano = %s", (valor,))
        elif opcao == '4':
            cursor.execute("SELECT * FROM tb_produto")
        else:
            print("Opção inválida!")
            return
        
        resultados = cursor.fetchall()
        
        if not resultados:
            print("\nNenhum produto encontrado com os critérios especificados.")
        else:
            print("\nResultados da busca:")
            print("-" * 95)
            print(f"{'ID':<5}{'Nome':<15}{'preço':<15}{'data de validade':<12}")
            print("-" * 95)
            for prod in resultados:
                print(f"{prod['idt']:<5}{prod['nome']:<15}"
                      f"{prod['preco']:<10}"
                      f"{prod['data_validade'].strftime('%Y-%m-%d') if prod['data_validade'] else 'N/D':<12}")
    except Error as e:
        print(f"Erro ao consultar produtos: {e}")
    finally:
        cursor.close()

def consultar_carros(conn):
    try:
        cursor = conn.cursor()

        sql = "SELECT * FROM tb_produto"

        cursor.execute(sql)

        resultado = cursor.fetchall()

        if not resultado:
            print("tabela vazia.")

        else:
            for func in resultado:
                print(func)
                print("-" * 35)

            for func in resultado:
                print("ID:", func[0])
                print("Nome:", func[1])
                print("preço:", func[2])
                print("data de validade:", func[3])
                print("-"*35)
    except Error as e:
        print(f"Erro ao consultar produtos: {e}")
    
def main():
    conn = conectar_banco()
    if conn is None:
        return
    
    while True:
        print("\nMenu loja:")
        print("1 - Consultar produtos com filtro")
        print("2 - Consultar produtos sem filtro")
        print("3 - Sair")
        
        escolha = input("Escolha uma opção (1-3): ")
        
        if escolha == '1':
            consultar_carros_filtro(conn)
        elif escolha == "2":
            consultar_carros(conn)
        elif escolha == '3':
            os.system("cls")
            break
        else:
            print("Opção inválida!")
    
    conn.close()
    print("\nPrograma encerrado.")



if __name__ == "__main__":
    main()