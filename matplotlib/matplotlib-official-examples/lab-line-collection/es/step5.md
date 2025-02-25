# Asignar colores a valores

También podemos asignar un array de valores a colores usando la función `ScalarMappable.set_array`. Crearemos un nuevo conjunto de datos y un nuevo objeto `LineCollection` con el parámetro `array` establecido en los valores de `x`. Luego podemos usar el método `colorbar` del objeto `Figure` para agregar una barra de colores a la gráfica.

```python
N = 50
x = np.arange(N)
ys = [x + i for i in x]
segs = [np.column_stack([x, y]) for y in ys]

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

line_segments = LineCollection(segs, array=x,
                               linewidths=(0.5, 1, 1.5, 2),
                               linestyles='solid')
ax.add_collection(line_segments)
axcb = fig.colorbar(line_segments)
axcb.set_label('Line Number')
ax.set_title('Line Collection with mapped colors')
plt.sci(line_segments)
plt.show()
```
