# Ajoutez une annotation fléchée

Nous allons maintenant ajouter une annotation fléchée au tracé. Le code suivant ajoutera une flèche du premier point de données au second point de données.

```python
ax.annotate("", xy=(1, 3), xytext=(2, 4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
```
