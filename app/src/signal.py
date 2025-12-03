from serial import Serial
import matplotlib.pyplot as plt

class Signal:
    def __init__(self, baudrate: int =115200, port: str = "COM3"):
        self.baudrate = baudrate
        self.port = port
        self.ser = Serial(self.port, self.baudrate, timeout=1)
    
    def leer_linea(self) -> str:
        linea = self.ser.readline()
        return linea.decode("utf-8").strip()

    def leer_valores(self) -> list[float]:
        linea = self.leer_linea()
        if linea.startswith('[') and linea.endswith(']'):
            valores = linea[1:-1].split(',')
            respuesta = [float(v.strip()) for v in valores]
            return respuesta
        return []
    
    def stream(self):
        plt.ion() # Activa el modo interactivo de Matplotlib

        fig, ax = plt.subplots()
        while True:
            valores = self.leer_valores()
            if valores:
                ax.clear()
                ax.plot(valores, marker="o")
                ax.set_ylim(0, 1) # Asume que los valores están entre 0 y 1
                ax.set_title('Valores ADC')
                ax.set_xlabel('Muestras')
                ax.set_ylabel('Voltios')
                plt.pause(0.01) # Pequeña pausa para actualizar la gráfica