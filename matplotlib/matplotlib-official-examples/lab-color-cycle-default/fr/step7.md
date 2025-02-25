# Personnalisez les repères de l'axe y

Nous personnalisons les repères de l'axe y pour les sous-graphiques les plus à gauche.

```python
for irow in range(2):
    axs[irow, 0].yaxis.set_ticks(np.arange(0, 10, 2))
```
