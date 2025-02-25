# Construire le nuage de points

Maintenant, nous allons construire le nuage de points que nous mettrons à jour pendant l'animation au fur et à mesure que les gouttes de pluie évoluent.

```python
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=0.5, edgecolors=rain_drops['color'],
                  facecolors='none')
```
