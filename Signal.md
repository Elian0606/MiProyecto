# 📡 Documentación del Módulo Signal (`signal.py`)

Este módulo contiene la clase `Signal`, la cual es crucial para establecer la **comunicación serial** (PySerial) y la **visualización de datos en tiempo real** (Matplotlib), transformando los datos recibidos del microcontrolador en gráficos dinámicos.

## Explicación Detallada del Código

1. Método __init__ (Constructor)
Propósito: Inicializar la conexión serial.

Acción: Crea el objeto Serial utilizando el puerto y la velocidad especificados. El timeout=1 asegura que la lectura no se bloquee indefinidamente.

2. Método leer_valores
Propósito: Parsear la cadena de texto serial a una lista de números flotantes.

Proceso:

Llama a self.leer_linea() (que lee los datos del puerto y los decodifica a una cadena).

Verifica que la línea tenga el formato de lista ([... ]).

Remueve los corchetes (linea[1:-1]) y usa .split(',') para separar los valores.

Utiliza una comprensión de lista para convertir cada valor a un número float, preparándolo para ser graficado.

3. Método stream
Propósito: Dibujar y actualizar la gráfica en tiempo real.

Acciones Necesarias:

plt.ion(): Habilita el modo interactivo de Matplotlib, permitiendo que la ventana de la gráfica se mantenga abierta y se actualice.

while True: Bucle infinito que mantiene la aplicación leyendo y dibujando datos continuamente.

ax.clear(): Borra el contenido de la gráfica del ciclo anterior.

plt.pause(0.01): Introduce una pausa mínima para forzar la actualización de la ventana, lo que crea el efecto de streaming.

## Código de la Clase Signal

```python
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
        plt.ion() # Activa el modo interactivo

        fig, ax = plt.subplots()
        while True:
            valores = self.leer_valores()
            if valores:
                ax.clear()
                ax.plot(valores, marker="o")
                ax.set_ylim(0, 1)
                ax.set_title('Valores ADC')
                ax.set_xlabel('Muestras')
                ax.set_ylabel('Voltios')
                plt.pause(0.01) # Pausa para actualizar la gráfica```