# Generar datos

En este paso, generaremos los datos para el gráfico de líneas. Utilizaremos la función `arange()` de NumPy para generar una matriz de valores para el eje x, y la función `sin()` para generar una matriz de valores para el eje y de una onda senoidal.

```python
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
```
