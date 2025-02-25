# Crear un gráfico de pastel anidado utilizando `ax.pie`

Podemos crear un gráfico de pastel anidado utilizando el método `ax.pie`. Primero generaremos algunos datos falsos, correspondientes a tres grupos. En el círculo interior, consideraremos cada número como perteneciente a su propio grupo. En el círculo exterior, los graficaremos como miembros de sus 3 grupos originales.

```python
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()
```
