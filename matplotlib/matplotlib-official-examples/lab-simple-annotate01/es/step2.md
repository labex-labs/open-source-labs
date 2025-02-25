# Crear un gráfico

Ahora crearemos un gráfico para agregar anotaciones. El siguiente código creará un gráfico con dos puntos de datos.

```python
fig, ax = plt.subplots()
x = [1, 2]
y = [3, 4]
ax.plot(x, y, "o")
```
