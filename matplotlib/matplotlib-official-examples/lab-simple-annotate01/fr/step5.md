# Ajoutez une annotation de forme

Nous allons maintenant ajouter une annotation de forme au tracé. Le code suivant ajoutera un rectangle autour du second point de données.

```python
bbox = dict(boxstyle="round", fc="0.8")
ax.annotate("Point de données 2", xy=(2, 4), xytext=(2.5, 4.5),
            bbox=bbox,
            arrowprops=dict(facecolor="black", shrink=0.05))
```
