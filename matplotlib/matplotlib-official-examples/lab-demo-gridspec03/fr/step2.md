# Générer des sous-graphiques avec `GridSpec`

Dans cette étape, nous allons utiliser `GridSpec` pour générer des sous-graphiques. Nous allons créer une figure avec 2 lignes et 2 colonnes. Nous spécifierons également les `width_ratios` et les `height_ratios` pour contrôler les tailles relatives des sous-graphiques.

```python
fig = plt.figure()
gs = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
```
