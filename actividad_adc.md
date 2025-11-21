# Informe:
Conversor Analogico-Digital (ADC) con Raspberry Pi Pico
## 1 Introduccion:
El presente informe analiza una implementación en MicroPython para la gestión de 
conversiones analógico-digitales (ADC) en sistemas embebidos. El código examinado demuestra 
principios fundamentales de adquisición de señales analógicas, procesamiento digital y 
encapsulación de funcionalidades mediante programación orientada a objetos. Esta 
implementación resulta particularmente relevante en aplicaciones de instrumentación, sistemas de 
monitorización y control de procesos industriales donde la interfaz con sensores analógicos es 
esencial. 
La solución propuesta aprovecha las capacidades del hardware de microcontroladores 
modernos, específicamente el ADC integrado, proporcionando una abstracción software que 
facilita la reutilización del código y mantiene la eficiencia requerida en sistemas embebidos. 

## 2 Codigo:

```python
from machine import ADC, Pin
import time

class ConversorADC:

    def __init__(self, pin_adc=26):
        self.adc = ADC(Pin(pin_adc))
        self.resolucion = 16
        self.vref = 3.3

    def leer_raw(self):
        """Lee valor ADC sin procesar (0-65535)"""
        return self.adc.read_u16()

    def leer_voltaje(self):
        """Convierte a voltaje (0-3.3V)"""
        raw = self.leer_raw()
        return (raw * self.vref) / 65535

    def leer_porcentaje(self):
        """Convierte a porcentaje (0-100%)"""
        raw = self.leer_raw()
        return (raw / 65535) * 100

    def leer_12bits(self):
        """Convierte a resolución nativa de 12 bits (0-4095)"""
        raw = self.leer_raw()
        return raw >> 4

adc = ConversorADC(26)

while True:
    raw = adc.leer_raw()
    voltaje = adc.leer_voltaje()
    porcentaje = adc.leer_porcentaje()
    bits12 = adc.leer_12bits()

    print(f'RAW: {raw:5d} | {voltaje:.2f} V | {porcentaje:.1f}% | 12b: {bits12:4d}")
    time.sleep(0.5)
```
## 3. DESCRIPCIÓN DEL CÓDIGO

### 3.1. Importación de Módulos y Dependencias

El código de importación es el siguiente:
python
from machine import ADC, Pin
import tim 
1. Importación de Módulos y Dependencias 
 
from machine import ADC, Pin import time 
Análisis Técnico: 
•	machine: Módulo fundamental de MicroPython que proporciona acceso directo al hardware y periféricos del microcontrolador. 
•	ADC: Clase especializada para controlar el conversor analógico-digital del sistema. 
•	Pin: Clase para gestión de pines de E/S, esencial para configurar el canal ADC. 
•	time: Módulo estándar que proporciona funciones de temporización, crucial para el muestreo periódico. 
 
2. Definición de la Clase ConversorADC 
 
Constructor e Inicialización 
def __init__(self, pin_adc=26):     self.adc = ADC(Pin(pin_adc))     self.resolucion = 16     self.vref = 3.3 
Funcionamiento y estructura: 
•	Parámetro pin_adc: Especifica el pin GPIO conectado al ADC (valor por defecto 26, común en Raspberry Pi Pico). 
•	Instanciación del ADC: ADC(Pin(pin_adc)) configura el hardware para funcionar como entrada analógica. 
•	Resolución: Establecida en 16 bits, correspondiente al rango completo del ADC (0-65535). • Voltaje de referencia (vref): 3.3V, valor típico en microcontroladores de 3.3V, determina el rango de medida. 
 
Método leer_raw() 
def leer_raw(self): 
    """Lee valor ADC sin procesar (0-65535)"""     return self.adc.read_u16() 
Características técnicas: 
•	read_u16(): Método nativo que retorna un valor entero sin signo de 16 bits. 
•	Rango de salida: 0 a 65535 (2^16 - 1), representando la cuantización completa del ADC. 
•	Resolución efectiva: Depende del hardware subyacente (generalmente 12 bits reales escalados a 16). 
 
Método leer_voltaje() 
def leer_voltaje(self): 
    """Convierte a voltaje (0-3.3V)"""     raw = self.leer_raw()     return (raw * self.vref) / 65535 
Procesamiento de señal: 
•	Fórmula de conversión: V = (valor_raw × Vref) / (2n - 1) 
•	Precisión: La división por 65535 (216 - 1) normaliza el valor raw al rango [0, Vref] 
•	Aplicación: Útil para interpretación directa de magnitudes físicas en voltios 
 
Método leer_porcentaje() 
def leer_porcentaje(self): 
    """Convierte a porcentaje (0-100%)"""     raw = self.leer_raw()     return (raw / 65535) * 100 
Transformación matemática: 
•	Normalización: raw / 65535 produce valor en rango [0, 1] 
•	Escalado lineal: Multiplicación por 100 para conversión a porcentaje 
•	Caso de uso: Ideal para potenciómetros, sensores de posición y indicadores 
 
Método leer_12bits() 
def leer_12bits(self): 
    """Convierte a resolución nativa de 12 bits (0-4095)"""     raw = self.leer_raw()     return raw >> 4 
Operación a nivel de bits: 
•	Desplazamiento derecho: >> 4 equivale a división entera por 16 (2^4) 
•	Justificación: Muchos ADCs internos tienen resolución nativa de 12 bits (0-4095) • Optimización: Operación computacionalmente eficiente versus división 
 
3. Implementación y Bucle Principal 
 
Instanciación del Objeto 
adc = ConversorADC(26) 
•	Canal ADC: Pin 26 seleccionado para adquisición 
•	Inicialización implícita: Todos los parámetros configurados con valores por defecto 
 
Bucle de Muestreo Continuo 
while True: 
    raw = adc.leer_raw()     voltaje = adc.leer_voltaje()     porcentaje = adc.leer_porcentaje()     bits12 = adc.leer_12bits()     print(f"RAW: {raw:5d} | {voltaje:.2f}V | {porcentaje:.1f}% | 12b: {bits
12:4d}")     time.sleep(0.5) 
Arquitectura de adquisición: 
•	Muestreo síncrono: Lectura secuencial de todas las representaciones 
•	Frecuencia de muestreo: 2 Hz (periodo de 500 ms) 
•	Formateo de salida: Presentación estructurada con especificadores de formato • Persistencia: Bucle infinito para monitorización continua 

 ## CONCLUSIONES 
 
 
La implementación analizada demuestra una arquitectura software robusta para aplicaciones de adquisición de datos en sistemas embebidos. La encapsulación en una clase proporciona modularidad, facilitando la reutilización y mantenimiento del código. La solución aborda eficientemente múltiples representaciones de los datos ADC (raw, voltaje, porcentaje, 12 bits), satisfaciendo diversos requisitos de aplicación. 
 
Desde la perspectiva de ingeniería de telecomunicaciones, el código muestra un uso apropiado de los recursos hardware, optimización computacional mediante operaciones de bits, y consideración de parámetros críticos como el voltaje de referencia. La estructura permite fácil extensión para incorporar funcionalidades adicionales como filtrado digital, calibración o gestión de múltiples canales ADC. 