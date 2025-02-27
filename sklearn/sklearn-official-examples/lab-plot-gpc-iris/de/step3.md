# Erstellen eines Gitters zum Plotten

Jetzt werden wir ein Gitter zum Plotten erstellen. Das Gitter wird verwendet werden, um die vorhergesagten Wahrscheinlichkeiten für jeden Punkt auf dem Gitter zu plotten. Wir definieren auch die Schrittweite für das Gitter.

```python
h = 0.02  # Schrittweite im Gitter

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
```
