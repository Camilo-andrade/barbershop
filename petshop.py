import serial

# Configurações da porta serial
port = 'COM3' # Substitua pela porta serial do seu Arduino
baudrate = 9600

# Inicializa a comunicação serial
ser = serial.Serial(port, baudrate)

try:
  while True:
    # Lê a linha de dados do Arduino
    line = ser.readline().decode('ascii').strip()
    
    # Verifica se a linha contém a temperatura
    if "Temperatura:" in line:
      # Extrai a temperatura do texto
      temp = float(line.split(":")[1].split(" ")[0])
      
      # Imprime a temperatura no terminal
      print("Temperatura: {:.1f} °C".format(temp))

except KeyboardInterrupt:
  # Fecha a conexão serial ao pressionar Ctrl+C
  ser.close()
  print("Programa encerrado.")