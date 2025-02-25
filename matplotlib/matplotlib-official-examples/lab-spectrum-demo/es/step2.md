# Establecer variables

A continuación, estableceremos las variables para nuestra señal. Utilizaremos un intervalo de muestreo de 0,01, lo que nos da una frecuencia de muestreo de 100 Hz. Crearemos una matriz de tiempo desde 0 hasta 10 segundos con un paso de 0,01 segundos. También generaremos ruido utilizando la función `randn` de NumPy y lo convolucionaremos con una función de decaimiento exponencial para crear una señal ruidosa.

```python
np.random.seed(0)

dt = 0.01  # intervalo de muestreo
Fs = 1 / dt  # frecuencia de muestreo
t = np.arange(0, 10, dt)

# generar ruido:
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)
cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]

s = 0.1 * np.sin(4 * np.pi * t) + cnse  # la señal
```
