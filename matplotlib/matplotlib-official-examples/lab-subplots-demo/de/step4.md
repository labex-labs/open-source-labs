# Achsen teilen

Standardmäßig wird jede `Achse` einzeln skaliert. Um die horizontale oder vertikale Achse von Subplots auszurichten, können wir die Parameter `sharex` oder `sharey` verwenden.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(x, y)
ax2.plot(x + 1, -y)
```
