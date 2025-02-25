# Définissez les paramètres du diagramme en barres

L'étape suivante est de définir les paramètres du diagramme en barres. Nous allons définir les emplacements x pour les groupes, la largeur des barres et les étiquettes pour les graduations de l'axe x.

```python
ind = np.arange(N)    # les emplacements x pour les groupes
width = 0.35         # la largeur des barres
ax.set_xticks(ind + width / 2, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
```
