# Graficar la correlación cruzada

Ahora graficaremos la correlación cruzada entre los dos arrays utilizando la función `xcorr` en Matplotlib.

```python
fig, ax = plt.subplots()
ax.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
ax.grid(True)
plt.show()
```

La función `xcorr` toma los siguientes parámetros:

- `x`: el primer array de datos
- `y`: el segundo array de datos
- `usevlines`: booleano, indica si se deben graficar líneas verticales desde 0 hasta el valor de correlación
- `maxlags`: entero, el número máximo de retrasos para calcular la correlación
- `normed`: booleano, indica si se deben normalizar los valores de correlación
- `lw`: entero, el ancho de línea para la gráfica
