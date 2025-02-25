# Den Pfeilplot erstellen

Wir können den Pfeilplot mit der Funktion `ax.quiver()` erstellen. Wir übergeben die Arrays `X`, `Y`, `U` und `V` als Parameter.

```python
fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V)
```
