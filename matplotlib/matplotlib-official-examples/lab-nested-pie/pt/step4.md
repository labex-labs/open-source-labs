# Personalizar o Gráfico de Pizza Aninhado

Podemos personalizar o gráfico de pizza aninhado alterando as cores, adicionando rótulos e ajustando o tamanho.

```python
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

# Add labels
labels = ['Group 1', 'Group 2', 'Group 3']
ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'), labels=labels, labeldistance=0.7)

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'))

# Set the title
ax.set(aspect="equal", title='Nested Pie Chart')

plt.show()
```
