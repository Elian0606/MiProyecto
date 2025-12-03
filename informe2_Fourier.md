# Transformada Discreta de Fourier (DFT)

## ¿QUÉ CAMBIAMOS?

Cambiamos el nombre de la clase de TDF a TransformadaFourier y modificamos el constructor para que ahora reciba las muestras de la señal junto con la frecuencia de muestreo, en lugar de solo la frecuencia. Transformamos el método calcular() en el método interno _calcular_dft() que se ejecuta automáticamente al crear el objeto. Eliminamos por completo el cálculo de magnitudes, fases, separación de coeficientes pares/impares y el análisis espectral detallado. Renombramos variables: x por muestras, fs por frecuencia_muestreo, X por XK, y simplificamos el caso de prueba de una señal multicomponente compleja a una simple senoidal de 2Hz.

## ¿POR QUÉ SE HICIERON ESTOS CAMBIOS?

Los cambios se realizaron para adoptar un paradigma más orientado a objetos, donde la transformada se conceptualiza como una entidad con estado propio rather que como una calculadora utilitaria. La nueva nomenclatura busca mejorar la legibilidad y autodocumentación del código, haciendo que los nombres sean más descriptivos para desarrolladores que no estén familiarizados con el dominio. La eliminación de funcionalidades complejas respondió a una decisión de simplificación, enfocándose en el cálculo core de la DFT mientras se delega el análisis especializado a métodos futuros o clases derivadas, creando así una base más limpia y mantenible para extensiones posteriores.

## Codigo
```python
import math
import cmath

class TransformadaFourier:
    
    def __init__(self, muestras, frecuencia_muestreo):
        self.muestras = muestras
        self.frecuencia_muestreo = frecuencia_muestreo
        self.N = len(muestras)
        self.coeficientes = self._calcular_dft()
    
    def _calcular_dft(self):
        XK = []
        for K in range(self.N):
            suma = 0 + 0j 
            for n in range(self.N):
                exponente = -2j * cmath.pi * n * K / self.N
                suma += self.muestras[n] * cmath.exp(exponente)
            XK.append(suma)
        return XK

    def mostrar_valores(self):
        print("Valores específicos de la DFT:")
        print(f"N = {self.N}, Fs = {self.frecuencia_muestreo} Hz")
        print("\nPrimeros 5 coeficientes:")
        for i in range(5):
            coef = self.coeficientes[i]
            print(f"K={i}: {coef} | Magnitud: {abs(coef)}")


if __name__ == "__main__":
    fs = 100
    t = [i/fs for i in range(100)]
    señal = [math.sin(2 * math.pi * 2 * t_i) for t_i in t]
    
    tf = TransformadaFourier(señal, fs)
    tf.mostrar_valores()
```