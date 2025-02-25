# Erstellen eines Scatterplots mit mehreren Gruppen

Wir können einen Scatterplot mit mehreren Gruppen erstellen, indem wir durch jede Gruppe iterieren und für jede Gruppe einen Scatterplot erstellen. Wir legen die Farbe, die Größe und die Transparenz der Marker für jede Gruppe mithilfe der Parameter `c`, `s` und `alpha` fest. Wir legen auch den Parameter `label` auf den Gruppennamen fest, der in der Legende verwendet werden wird.

```python
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
```
