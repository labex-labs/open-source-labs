# Erstellen eines geschachtelten Kreisdiagramms mit `ax.pie`

Wir können ein geschach teltes Kreisdiagramm mit der `ax.pie`-Methode erstellen. Zunächst werden wir einige simulierte Daten generieren, die drei Gruppen entsprechen. Im inneren Kreis werden wir jede Zahl als eigene Gruppe behandeln. Im äußeren Kreis werden wir sie als Mitglieder ihrer ursprünglichen 3 Gruppen darstellen.

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
