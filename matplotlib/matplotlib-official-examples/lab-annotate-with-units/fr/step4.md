# Ajoutez une annotation de flèche avec des coordonnées xy et du texte unitaires

Dans cette étape, nous allons ajouter une annotation de flèche au graphique à l'aide de la fonction `annotate()`. Nous fournirons la position de la flèche, le texte à afficher et les propriétés de la flèche. Nous spécifierons également les unités de mesure pour la position et le texte.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8*cm, 0.95*cm), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
