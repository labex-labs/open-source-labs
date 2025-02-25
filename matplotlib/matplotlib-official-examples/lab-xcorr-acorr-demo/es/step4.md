# Graficar la autocorrelación

Ahora graficaremos la autocorrelación del array `x` utilizando la función `acorr` en Matplotlib.

```python
fig, ax = plt.subplots()
ax.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax.grid(True)
plt.show()
```

La función `acorr` toma los siguientes parámetros:

- `x`: el array de datos para calcular la autocorrelación
- `usevlines`: booleano, indica si se deben graficar líneas verticales desde 0 hasta el valor de correlación
- `normed`: booleano, indica si se deben normalizar los valores de correlación
- `maxlags`: entero, el número máximo de retrasos para calcular la correlación
- `lw`: entero, el ancho de línea para la gráfica
