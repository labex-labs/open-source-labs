# Créer un graphique symlog sur l'axe x

Dans le premier sous-graphique, nous allons créer un graphique `symlog` sur l'axe x. Nous ajouterons également une grille mineure à l'axe x.

```python
ax0.plot(x, y1)
ax0.set_xscale('symlog')
ax0.set_ylabel('symlogx')
ax0.grid()
ax0.xaxis.grid(which='minor')
```
