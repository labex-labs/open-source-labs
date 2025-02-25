# Contrôler l'espacement autour et entre les sous-graphiques

Dans cette étape, nous allons utiliser `GridSpec` pour contrôler l'espacement autour et entre les sous-graphiques. Nous allons créer une figure avec 2 `gridspec`, chacun avec 3 lignes et 3 colonnes. Nous spécifierons les paramètres `left`, `right`, `bottom`, `top`, `wspace` et `hspace` pour contrôler l'espacement.

```python
fig = plt.figure()
gs1 = GridSpec(3, 3, left=0.05, right=0.48, wspace=0.05)
ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = GridSpec(3, 3, left=0.55, right=0.98, hspace=0.05)
ax4 = fig.add_subplot(gs2[:, :-1])
ax5 = fig.add_subplot(gs2[:-1, -1])
ax6 = fig.add_subplot(gs2[-1, -1])
```
