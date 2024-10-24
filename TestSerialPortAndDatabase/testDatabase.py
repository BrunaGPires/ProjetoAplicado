import sqlite3

def test_connection():
    try:
        print("Tentando conectar ao banco de dados SQLite...")
        # Conectando-se ao banco de dados (um será criado se não existir)
        db = sqlite3.connect('C:/Users/GamePlay/estoque.db')

        # Verificando a conexão e executando um comando simples
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            print("Conexão com o banco de dados SQLite estabelecida com sucesso!")
            print("Tabelas existentes:", tables)
        else:
            print("Nenhuma tabela encontrada no banco de dados.")
        
        db.close()
    except sqlite3.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

test_connection()