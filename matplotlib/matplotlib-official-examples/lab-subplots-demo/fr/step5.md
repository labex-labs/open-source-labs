# Axes polaires

Nous pouvons créer une grille d'`Axes` polaires en passant le paramètre `projection='polar'` à la fonction `subplots()`.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)
```
