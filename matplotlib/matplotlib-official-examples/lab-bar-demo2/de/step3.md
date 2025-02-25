# Erstellen des Balkendiagramms mit Standardmaßen

In diesem Schritt werden wir das Balkendiagramm mit Standardmaßen mithilfe der `bar`-Methode von Matplotlib erstellen. Wir werden den Parameter `bottom` verwenden, um die untere Grenze der Balken auf 0 zu setzen.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].bar(cms, cms, bottom=bottom)
```
