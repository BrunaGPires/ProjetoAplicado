import serial
import sqlite3
import time

# Função para atualizar o estoque no banco de dados SQLite
def update_stock():
    try:
        db_connection = sqlite3.connect('C:/Users/GamePlay/estoque.db')
        cursor = db_connection.cursor()
        cursor.execute("UPDATE produtos SET quantidade = quantidade - 1 WHERE nome = 'bateria'")
        db_connection.commit()
        db_connection.close()
        print("Estoque atualizado no banco de dados.")
    except sqlite3.Error as e:
        print(f"Erro ao conectar/atualizar o banco de dados: {e}")

# Função para monitorar a porta serial e atualizar o banco de dados
def monitor_serial():
    try:
        ser = serial.Serial('COM6', 115200, timeout=1)
        print("Porta serial aberta:", ser.portstr)

        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(f"Dado recebido: {line}")

                # Verificando se a palavra "bateria" está nos dados recebidos
                if "bateria" in line.lower():
                    print("Bateria detectada, atualizando estoque...")
                    update_stock()
                else:
                    print("Nenhuma ação necessária.")
                    
            # Pausa antes de verificar novamente
            time.sleep(1)  
    except serial.SerialException as e:
        print(f"Erro ao acessar a porta serial: {e}")
    finally:
        ser.close()
        print("Porta serial fechada.")

monitor_serial()