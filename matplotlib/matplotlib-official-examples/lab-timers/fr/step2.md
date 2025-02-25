# Définir la fonction pour mettre à jour le titre

Définir la fonction pour mettre à jour le titre de la figure avec l'heure actuelle.

```python
def update_title(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()
```
