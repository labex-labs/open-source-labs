# Effectuer une rotation d'image

Dans cette étape, nous effectuons une rotation de l'image à l'aide de la fonction `rotate_deg`. Nous passons l'angle de rotation en tant qu'entrée à la fonction `rotate_deg`. Nous utilisons la fonction `do_plot` pour afficher l'image tournée.

```python
# préparer l'image et la figure
fig, ax1 = plt.subplots()
Z = get_image()

# rotation de l'image
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))
```
