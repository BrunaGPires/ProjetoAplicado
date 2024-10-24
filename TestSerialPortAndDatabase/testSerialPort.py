import serial

def test_serial():
    try:
        # Inicializando a porta serial 
        ser = serial.Serial('COM6', 115200, timeout=1)
        print("Porta serial aberta:", ser.portstr)
        line = ser.readline()
        print("Dados recebidos da serial:", line.decode('utf-8').strip())
        ser.close()
    except serial.SerialException as e:
        print(f"Erro ao acessar a porta serial: {e}")

test_serial()