# Criar um gráfico de pizza aninhado usando `ax.pie`

Podemos criar um gráfico de pizza aninhado usando o método `ax.pie`. Primeiro, geraremos alguns dados falsos, correspondentes a três grupos. No círculo interno, trataremos cada número como pertencente ao seu próprio grupo. No círculo externo, os plotaremos como membros de seus 3 grupos originais.

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
