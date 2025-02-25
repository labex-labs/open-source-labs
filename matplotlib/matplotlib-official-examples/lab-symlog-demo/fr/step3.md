# Créer des graphiques

Maintenant que nous avons nos données, nous pouvons créer nos graphiques. Nous allons créer trois sous-graphiques, chacun avec une mise à l'échelle de l'axe `symlog` différente.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3)
```
