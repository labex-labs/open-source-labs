# Ajoutez une annotation de flèche avec des unités mixtes

Dans cette étape, nous allons ajouter une autre annotation de flèche au graphique à l'aide de la fonction `annotate()`. Nous fournirons la position de la flèche, le texte à afficher et les propriétés de la flèche. Nous allons également mélanger les unités de mesure pour la position et utiliser la fraction d'axes pour le texte.

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
