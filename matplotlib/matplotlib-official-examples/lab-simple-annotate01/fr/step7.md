# Positionnez les annotations

Nous pouvons positionner les annotations en utilisant différents systèmes de coordonnées. Le code suivant positionnera l'annotation de texte en utilisant les coordonnées de données et l'annotation fléchée en utilisant les coordonnées de la figure.

```python
ax.annotate("Point de données 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="data")
ax.annotate("", xy=(1, 3), xytext=(0.5, 0.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="figure fraction")
```
