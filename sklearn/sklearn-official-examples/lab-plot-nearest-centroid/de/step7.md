# Zeichne die Datenpunkte

Wir zeichnen die Eingabedatenpunkte mit der scatter-Funktion aus Matplotlib.

```python
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor="k", s=20)
```
