# Etiquetado de barras usando una cadena de formato con `{}`

En este paso, mostraremos cómo usar una cadena de formato con `{}` para formatear las etiquetas de barras. Usaremos algunos datos sobre las ventas de helado por sabor.

```python
fruit_names = ['Coffee', 'Salted Caramel', 'Pistachio']
fruit_counts = [4000, 2000, 7000]

fig, ax = plt.subplots()
bar_container = ax.bar(fruit_names, fruit_counts)
ax.set(ylabel='pints sold', title='Gelato sales by flavor', ylim=(0, 8000))
ax.bar_label(bar_container, fmt='{:,.0f}')
```
