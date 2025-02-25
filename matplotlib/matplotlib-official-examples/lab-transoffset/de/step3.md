# Ein Streudiagramm erstellen

Wir werden nun ein Streudiagramm erstellen, indem wir die `plot`-Funktion aus `matplotlib.pyplot` verwenden.

```python
fig = plt.figure(figsize=(5, 10))
ax = plt.subplot(2, 1, 1)

# Plot the data
for x, y in zip(xs, ys):
    plt.plot(x, y, 'ro')
```
