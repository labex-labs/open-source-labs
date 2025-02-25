# Representar el código de barras

Finalmente, podemos representar el código de barras usando `Axes.imshow`. Usaremos `code.reshape(1, -1)` para convertir los datos en una matriz bidimensional con una sola fila, `imshow(..., aspect='auto')` para permitir píxeles no cuadrados y `imshow(..., interpolation='nearest')` para evitar bordes borrosos.

```python
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
plt.show()
```
