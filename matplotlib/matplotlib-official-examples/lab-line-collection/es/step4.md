# Crear la gráfica

Ahora podemos crear una gráfica usando `matplotlib` y agregar el objeto `LineCollection` a la gráfica usando el método `add_collection` del objeto `Axes`.

```python
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(ys.min(), ys.max())

ax.add_collection(line_segments)
ax.set_title('Line collection with masked arrays')
plt.show()
```
