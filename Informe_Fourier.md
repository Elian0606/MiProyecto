Informe_Fourier.md
# Análisis e Implementación de la Transformada Discreta de Fourier (TDF)

Este código implementa una Transformada Discreta de Fourier (TDF) desde cero, incluyendo funcionalidades para analizar y clasificar los resultados obtenidos.

## Función del código

El objetivo principal de este código es analizar señales para identificar qué frecuencias contienen y qué tan intensas son cada una. Transforma una señal mezclada en el tiempo en una lista clara de sus componentes frecuenciales, como detectar los ingredientes exactos de una receta compleja.

## ¿Cómo trabaja el código?

### Crea la señal de prueba

El código genera una señal que combina cuatro componentes diferentes: una señal constante, dos tonos específicos de 10Hz y 25Hz, y un pequeño ruido de 37Hz. Toma 16 muestras de esta señal a lo largo del tiempo.

### Configura el analizador

Se crea un objeto TDF con una frecuencia de muestreo de 100Hz, lo que significa que puede analizar señales hasta de 50Hz.

### Calcula las coincidencias frecuenciales

Para cada frecuencia posible (desde 0Hz hasta 93.75Hz en pasos de 6.25Hz), el código prueba qué tanto se parece la señal original a una onda seno/coseno de esa frecuencia específica.

### Realiza las multiplicaciones y sumas

En un proceso de doble bucle, multiplica cada muestra de la señal por el valor correspondiente de la onda de prueba y suma todos estos productos. Si la señal contiene esa frecuencia, la suma será grande.

### Procesa los resultados

Convierte los números complejos resultantes en magnitudes (qué tan fuerte es cada frecuencia) y fases.

## Código.
```python
import math
import cmath

class TDF:
    def __init__(self, fs=100):
        self.fs = fs
    
    def calcular(self, x):
        """Calcula TDF y retorna magnitudes, fases, pares e impares"""
        N = len(x)
        X = []
        
        for k in range(N):
            suma = 0
            for n in range(N):
                exp = -2j * cmath.pi * k * n / N
                suma += x[n] * cmath.exp(exp)
            X.append(suma)
        
        
        pares = []
        impares = []
        
        for k in range(N):
            if k % 2 == 0:
                pares.append(X[k])
            else:
                impares.append(X[k])
        
        mag = [abs(x) for x in X]
        fase = [cmath.phase(x) * 180 / cmath.pi for x in X]
        
        return mag, fase, X, pares, impares


if __name__ == "__main__":
    print("=== PRUEBA DE TRANSFORMADA DISCRETA DE FOURIER ===\n")
    
    fs = 100  
    N = 16    
    t = [i/fs for i in range(N)]  
    
    señal = []
    for t_i in t:
        componente_10Hz = 2.0 * math.cos(2 * math.pi * 10 * t_i)
        componente_25Hz = 1.0 * math.sin(2 * math.pi * 25 * t_i)
        componente_DC = 0.5  
        ruido = 0.1 * math.sin(2 * math.pi * 37 * t_i) 
        señal.append(componente_10Hz + componente_25Hz + componente_DC + ruido)
    
    print(f"Señal de entrada ({N} muestras):")
    for i, valor in enumerate(señal):
        print(f"  Muestra {i:2d}: {valor:7.3f}")
    
    tdf = TDF(fs=fs)
    mag, fase, X, pares, impares = tdf.calcular(señal)
    
    print(f"\nResultados de la TDF:")
    print(f"{'k':>2} {'Frec (Hz)':>8} {'Magnitud':>10} {'Fase (°)':>10} {'Par/Impar':>10}")
    print("-" * 60)
    
    for k in range(N):
        freq = k * fs / N
        tipo = "PAR" if k % 2 == 0 else "IMPAR"
        print(f"{k:2d} {freq:8.2f} {mag[k]:10.4f} {fase[k]:10.2f} {tipo:>10}")
    
    print(f"\nResumen de pares e impares:")
    print(f"Coeficientes pares (k par): {len(pares)} elementos")
    print(f"Coeficientes impares (k impar): {len(impares)} elementos")
    
    print(f"\nMagnitud promedio pares: {sum(abs(x) for x in pares)/len(pares):.4f}")
    print(f"Magnitud promedio impares: {sum(abs(x) for x in impares)/len(impares):.4f}")
```