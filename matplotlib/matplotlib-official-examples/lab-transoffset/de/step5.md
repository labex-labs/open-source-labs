# Ein Polardiagramm erstellen

Wir werden nun ein Polardiagramm erstellen, indem wir die `polar`-Funktion aus `matplotlib.pyplot` verwenden.

```python
ax = plt.subplot(2, 1, 2, projection='polar')

# Plot the data
for x, y in zip(xs, ys):
    plt.polar(x, y, 'ro')
```
