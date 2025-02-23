# Annoter le graphique

Maintenant, nous allons annoter le graphique en ajoutant une flèche pointant vers une coordonnée spécifique. Dans cet exemple, nous allons ajouter une flèche pointant vers le maximum local de la fonction cosinus.

```python
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
```

La fonction `ax.annotate()` prend plusieurs arguments. Le premier argument est le texte qui sera affiché sur le graphique. L'argument `xy` spécifie les coordonnées du point que nous voulons annoter. L'argument `xytext` spécifie les coordonnées du texte. L'argument `arrowprops` est un dictionnaire qui spécifie les propriétés de la flèche.
