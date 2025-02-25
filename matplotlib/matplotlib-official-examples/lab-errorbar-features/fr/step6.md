# Tracer une échelle logarithmique avec des barre d'erreur

Enfin, nous allons tracer nos données avec une échelle logarithmique et des barre d'erreur. La fonction `ax.set_yscale()` est utilisée pour définir l'axe des y sur une échelle logarithmique.

```python
# plot log scale with error bars
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=error, fmt='o')
ax.set_title('Log Scale with Error Bars')
ax.set_yscale('log')
plt.show()
```
