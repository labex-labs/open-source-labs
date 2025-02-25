# Ajoutez une annotation de texte

Nous allons maintenant ajouter une annotation de texte au tracé. Le code suivant ajoutera le texte "Point de données 1" au premier point de données.

```python
ax.annotate("Point de données 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05))
```
