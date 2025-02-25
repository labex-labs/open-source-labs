# Création de sous-graphiques

Nous allons maintenant créer une grille 2x2 de sous-graphiques à l'aide de la fonction `subplots`. Cela nous donnera quatre graphiques pour visualiser le motif de rareté du tableau.

```python
fig, axs = plt.subplots(2, 2)
ax1 = axs[0, 0]
ax2 = axs[0, 1]
ax3 = axs[1, 0]
ax4 = axs[1, 1]
```
