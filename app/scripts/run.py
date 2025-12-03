import sys
import os

# --- BLOQUE CRUCIAL PARA ENCONTRAR MÓDULOS EN 'src' ---
# 1. Obtiene la ruta del directorio 'scripts'
script_dir = os.path.dirname(os.path.abspath(__file__))
# 2. Sube un nivel para obtener la raíz del proyecto ('analisis_serial')
project_root = os.path.dirname(script_dir) 
# 3. Agrega la raíz al PATH para que Python pueda encontrar 'src'
sys.path.insert(0, project_root)
# --------------------------------------------------------

from src.signal import Signal # Ahora funciona gracias al bloque de arriba

# Importaciones de librerías externas
import serial.tools.list_ports
import serial.tools.list_ports
import time

def detectar_puerto_serial():
    """Busca el primer puerto serie disponible."""
    puertos = serial.tools.list_ports.comports()
    
    if not puertos:
        print("❌ Error: No se detectaron puertos serie disponibles.")
        return None
    
    # Devuelve el nombre del primer puerto detectado
    puerto_detectado = puertos[0].device
    print(f"✅ Puerto detectado automáticamente: {puerto_detectado}")
    return puerto_detectado

if __name__ == "__main__":
    
    # 1. Detectar el puerto
    PORT_NAME = detectar_puerto_serial()
    
    if PORT_NAME is None:
        exit()

    # 2. Configuración
    BAUD_RATE = 115200 

    # 3. Intento de Conexión y Ejecución
    detector_senal = None # Inicializar para el bloque finally
    try:
        print(f"Intentando conectar a {PORT_NAME} a {BAUD_RATE} bps...")
        
        # Crear la instancia
        detector_senal = Signal(baudrate=BAUD_RATE, port=PORT_NAME)
        
        print("Conexión exitosa. Iniciando el streaming de datos...")
        detector_senal.stream()

    except serial.SerialException as e:
        print(f"\n🛑 Error de Conexión: No se pudo abrir el puerto {PORT_NAME}.")
        print(f"Asegúrate de que el dispositivo está conectado.")
        print(f"Detalle: {e}")
    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario.")
    finally:
        # 4. Cerrar la conexión
        if detector_senal is not None and detector_senal.ser.is_open:
            detector_senal.ser.close()
            print("Puerto serial cerrado.")