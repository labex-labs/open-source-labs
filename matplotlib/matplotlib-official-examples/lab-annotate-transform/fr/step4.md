# Transformer les coordonnées

L'étape suivante consiste à transformer les coordonnées des données et de l'affichage. Nous utiliserons la méthode `ax.transData` pour transformer les coordonnées des données et le système de coordonnées `pixels de la figure` pour transformer les coordonnées d'affichage.

```python
xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform((xdata, ydata))
```
