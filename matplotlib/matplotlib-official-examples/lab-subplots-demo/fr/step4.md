# Partage d'axes

Par défaut, chaque `Axes` est mis à l'échelle individuellement. Pour aligner l'axe horizontal ou vertical des sous-graphiques, nous pouvons utiliser les paramètres `sharex` ou `sharey`.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(x, y)
ax2.plot(x + 1, -y)
```
