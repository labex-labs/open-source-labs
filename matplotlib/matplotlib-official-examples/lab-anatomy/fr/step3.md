# Tracer les données

Maintenant, nous allons tracer nos données sur les axes que nous venons de créer. Nous utiliserons la méthode `plot()` pour tracer les trois ondes sinusoïdales avec différentes couleurs et largeurs de ligne.

```python
# Tracer les données
ax.plot(X, Y1, c='C0', lw=2.5, label="Blue signal", zorder=10)
ax.plot(X, Y2, c='C1', lw=2.5, label="Orange signal")
ax.plot(X[::3], Y3[::3], linewidth=0, markersize=9,
        marker='s', markerfacecolor='none', markeredgecolor='C4',
        markeredgewidth=2.5)
```
