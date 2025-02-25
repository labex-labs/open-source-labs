# Traçage du motif de rareté

Nous allons utiliser la fonction `spy` pour tracer le motif de rareté du tableau. Nous allons utiliser différents paramètres tels que `markersize` et `precision` pour personnaliser le tracé.

```python
ax1.spy(x, markersize=5)
ax2.spy(x, precision=0.1, markersize=5)
ax3.spy(x)
ax4.spy(x, precision=0.1)
```
