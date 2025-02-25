# Streudiagramm erstellen

In diesem Schritt erstellen wir ein Streudiagramm mit den zufälligen Daten aus Schritt 2.

```python
fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.scatter(x, y)
ax.set_aspect(1.)
```
