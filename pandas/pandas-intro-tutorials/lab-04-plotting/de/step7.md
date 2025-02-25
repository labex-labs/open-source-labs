# Erstellen von Teilplots für jede Spalte

Wir können separate Teilplots für jede der Datenspalten erstellen, indem wir das Argument `subplots` verwenden.

```python
# Creating subplots for each column
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```
