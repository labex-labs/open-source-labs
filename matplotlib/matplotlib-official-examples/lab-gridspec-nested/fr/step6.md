# Add Subplots to the Second Inner GridSpec

Nous allons maintenant ajouter des sous-graphes au deuxième gridspec interne. Nous allons créer trois sous-graphes : `ax4`, `ax5` et `ax6`.

```python
ax4 = fig.add_subplot(gs01[:, :-1])
ax5 = fig.add_subplot(gs01[:-1, -1])
ax6 = fig.add_subplot(gs01[-1, -1])
```
