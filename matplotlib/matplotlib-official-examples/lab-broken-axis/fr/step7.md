# Ajustement des graduations

Nous allons maintenant ajuster les graduations (ticks) sur l'axe des x. Nous allons déplacer les graduations du premier sous-graphique en haut en utilisant `ax1.xaxis.tick_top`, supprimer les étiquettes des graduations du premier sous-graphique en utilisant `ax1.tick_params(labeltop=False)` et conserver les étiquettes des graduations du deuxième sous-graphique.

```python
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()
```
