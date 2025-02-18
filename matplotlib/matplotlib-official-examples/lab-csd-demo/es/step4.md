# Calcular la Densidad Espectral Cruzada (CSD)

Para calcular la Densidad Espectral Cruzada (Cross Spectral Density, CSD) de dos señales, necesitamos utilizar la función `csd` de Matplotlib. La función toma las dos señales, el número de puntos para la Transformada Rápida de Fourier (FFT) y la frecuencia de muestreo como entradas.

```python
fig, ax = plt.subplots()
cxy, f = ax.csd(s1, s2, 256, 1. / dt)
ax.set_ylabel('CSD (dB)')
plt.show()
```
