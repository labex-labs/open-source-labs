# Ajoutez des sous-graphiques au GridSpec

Nous pouvons ajouter des sous-graphiques au GridSpec à l'aide de la fonction `fig.add_subplot()`. Nous pouvons spécifier l'emplacement du sous-graphique dans la grille en utilisant la notation d'indexation de l'objet GridSpec. Par exemple, `gs[0, :]` spécifie la première ligne et toutes les colonnes.

```python
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, :-1])
ax3 = fig.add_subplot(gs[1:, -1])
ax4 = fig.add_subplot(gs[-1, 0])
ax5 = fig.add_subplot(gs[-1, -2])
```
