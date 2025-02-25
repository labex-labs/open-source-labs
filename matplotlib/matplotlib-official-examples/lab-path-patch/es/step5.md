# Graficar puntos de control y líneas de conexión

En este paso, graficamos los puntos de control y las líneas de conexión de la ruta utilizando el método `plot` del objeto de ejes.

```python
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')
```
