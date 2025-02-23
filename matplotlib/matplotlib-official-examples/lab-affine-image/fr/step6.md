# Effectuer plusieurs transformations

Dans cette étape, nous effectuons plusieurs transformations de l'image à l'aide des fonctions `rotate_deg`, `skew_deg`, `scale` et `translate`. Nous passons les paramètres de transformation en tant qu'entrées aux fonctions respectives. Nous utilisons la fonction `do_plot` pour afficher l'image transformée.

```python
# préparer l'image et la figure
fig, ax4 = plt.subplots()
Z = get_image()

# tout et une translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1,.5).translate(.5, -1))
```
