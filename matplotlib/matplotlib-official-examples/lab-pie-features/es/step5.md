# Personalizar los colores

Podemos personalizar los colores de los segmentos pasando una lista de colores al parámetro `colors` de la función `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=['olivedrab', 'rosybrown', 'gray','saddlebrown'])
```
