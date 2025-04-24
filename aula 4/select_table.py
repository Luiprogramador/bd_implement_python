import mysql.connector
from mysql.connector import Error
import os

def conectar_banco():
    try:
        conn = mysql.connector.connect(
            user='root',
            password='lui1234',
            host='127.0.0.1',
            database='db_locadora'
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
    print("4 - Filtrar por estoque disponível")
    print("5 - Filtrar por quilometragem máxima")
    print("6 - Mostrar todos os carros")
    
    opcao = input("\nEscolha uma opção de filtro (1-6): ")
    
    try:
        cursor = conn.cursor(dictionary=True)
        
        if opcao == '1':
            valor = input("Digite o nome (ou parte) do carro: ")
            cursor.execute("SELECT * FROM tb_carro WHERE nome LIKE %s", (f'%{valor}%',))
        elif opcao == '2':
            valor = input("Digite a marca (ou parte) do carro: ")
            cursor.execute("SELECT * FROM tb_carro WHERE marca LIKE %s", (f'%{valor}%',))
        elif opcao == '3':
            valor = input("Digite o ano (AAAA-MM-DD): ")
            cursor.execute("SELECT * FROM tb_carro WHERE ano = %s", (valor,))
        elif opcao == '4':
            valor = input("Digite a quantidade mínima em estoque: ")
            cursor.execute("SELECT * FROM tb_carro WHERE qnt_estoque >= %s", (int(valor),))
        elif opcao == '5':
            valor = input("Digite a quilometragem máxima: ")
            cursor.execute("SELECT * FROM tb_carro WHERE qnt_km <= %s", (float(valor),))
        elif opcao == '6':
            cursor.execute("SELECT * FROM tb_carro")
        else:
            print("Opção inválida!")
            return
        
        resultados = cursor.fetchall()
        
        if not resultados:
            print("\nNenhum carro encontrado com os critérios especificados.")
        else:
            print("\nResultados da busca:")
            print("-" * 95)
            print(f"{'ID':<5}{'Nome':<15}{'Marca':<15}{'Ano':<12}{'Estoque':<10}{'KM':<10}")
            print("-" * 95)
            for carro in resultados:
                print(f"{carro['idt']:<5}{carro['nome']:<15}{carro['marca']:<15}"
                      f"{carro['ano'].strftime('%Y-%m-%d') if carro['ano'] else 'N/D':<12}"
                      f"{carro['qnt_estoque']:<10}{carro['qnt_km']:<10}")
    except Error as e:
        print(f"Erro ao consultar carros: {e}")
    finally:
        cursor.close()

def consultar_carros(conn):
    try:
        cursor = conn.cursor()

        sql = "SELECT * FROM tb_carro"

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
                print("Salario:", func[2])
                print("Idade:", func[3])
                print("Endereço:", func[4])
                print("-"*35)
    except Error as e:
        print(f"Erro ao consultar carros: {e}")
    
def main():
    conn = conectar_banco()
    if conn is None:
        return
    
    while True:
        print("\nMenu Locadora de Carros:")
        print("1 - Consultar carros com filtro")
        print("2 - Consultar carros sem filtro")
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