# Crear la primera gráfica

Ahora, creemos la primera gráfica usando `subplot`. `subplot` toma tres argumentos: el número de filas, el número de columnas y el número de la gráfica. En este ejemplo, crearemos una gráfica con 2 filas y 1 columna (`211`), lo que significa que la primera gráfica estará en la fila superior.

```python
ax1 = plt.subplot(211)
ax1.plot(t, np.sin(2*np.pi*t))
```
