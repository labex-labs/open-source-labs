# Charger l'image

Nous allons utiliser la méthode `get_sample_data` de `cbook` pour charger une image d'échantillonnage. Cette méthode renvoie un objet semblable à un fichier, que nous pouvons passer à `imshow` pour afficher l'image.

```python
with cbook.get_sample_data('grace_hopper.jpg') as image_file:
    image = plt.imread(image_file)
```
