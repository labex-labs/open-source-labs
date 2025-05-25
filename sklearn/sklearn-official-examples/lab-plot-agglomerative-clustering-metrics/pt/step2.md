# Plotar a rotulagem real

Plotamos a rotulagem real dos dados da forma de onda.

```python
n_clusters = 3

labels = ("Forma de Onda 1", "Forma de Onda 2", "Forma de Onda 3")

colors = ["#f7bd01", "#377eb8", "#f781bf"]

# Plotar a rotulagem real
plt.figure()
plt.axes([0, 0, 1, 1])
for l, color, n in zip(range(n_clusters), colors, labels):
    lines = plt.plot(X[y == l].T, c=color, alpha=0.5)
    lines[0].set_label(n)

plt.legend(loc="best")

plt.axis("tight")
plt.axis("off")
plt.suptitle("Verdade real", size=20, y=1)
```
