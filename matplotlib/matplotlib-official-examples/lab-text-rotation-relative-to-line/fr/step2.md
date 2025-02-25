# Ajuster les limites du graphique

Ensuite, nous allons ajuster les limites du graphique de sorte que la ligne diagonale ne soit plus à un angle de 45 degrés lorsqu'elle est vue à l'écran. Cela créera un scénario où nous devrons faire tourner le texte par rapport à la ligne, plutôt que par rapport au système de coordonnées de l'écran.

```python
# définir les limites de sorte qu'elle ne semble plus à 45 degrés à l'écran
ax.set_xlim([-10, 20])
```
