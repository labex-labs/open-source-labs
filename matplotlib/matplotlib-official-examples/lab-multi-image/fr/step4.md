# Mettre à jour les images

Enfin, nous allons mettre à jour les images pour qu'elles répondent aux changements dans la norme des autres images. Cela nous permettra de modifier la colormap et l'échelle de couleur d'une image et d'avoir toutes les autres mises à jour en conséquence.

```python
def update(changed_image):
    for im in images:
        if (changed_image.get_cmap()!= im.get_cmap()
                or changed_image.get_clim()!= im.get_clim()):
            im.set_cmap(changed_image.get_cmap())
            im.set_clim(changed_image.get_clim())

for im in images:
    im.callbacks.connect('changed', update)
```
