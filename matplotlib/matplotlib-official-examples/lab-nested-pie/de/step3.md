# Erstellen eines geschachtelten Kreisdiagramms mit `ax.bar`

Wir können auch ein geschach teltes Kreisdiagramm erstellen, indem wir die `ax.bar`-Methode auf Achsen mit einem polaren Koordinatensystem verwenden. Dies kann mehr Flexibilität bei der genauen Gestaltung des Diagramms bieten.

```python
fig, ax = plt.subplots(subplot_kw=dict(projection="polar"))

size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
# Normalisiere vals auf 2 pi
valsnorm = vals/np.sum(vals)*2*np.pi
# Bestimme die Ordinaten der Balkenränder
valsleft = np.cumsum(np.append(0, valsnorm.flatten()[:-1])).reshape(vals.shape)

cmap = plt.colormaps["tab20c"]
outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap([1, 2, 5, 6, 9, 10])

ax.bar(x=valsleft[:, 0],
       width=valsnorm.sum(axis=1), bottom=1-size, height=size,
       color=outer_colors, edgecolor='w', linewidth=1, align="edge")

ax.bar(x=valsleft.flatten(),
       width=valsnorm.flatten(), bottom=1-2*size, height=size,
       color=inner_colors, edgecolor='w', linewidth=1, align="edge")

ax.set(title="Pie plot with `ax.bar` and polar coordinates")
ax.set_axis_off()
plt.show()
```
