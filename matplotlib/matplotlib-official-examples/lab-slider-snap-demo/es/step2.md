# Generar datos

En este paso, generará los datos que se graficarán. Creará una onda sinusoidal con una frecuencia de 3 Hz y una amplitud de 5.

```python
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
s = a0 * np.sin(2 * np.pi * f0 * t)
```
