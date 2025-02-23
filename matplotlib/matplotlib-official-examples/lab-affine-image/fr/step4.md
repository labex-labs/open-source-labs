# Effectuer une distorsion d'image

Dans cette étape, nous effectuons une distorsion de l'image à l'aide de la fonction `skew_deg`. Nous passons les angles de distorsion en tant qu'entrées à la fonction `skew_deg`. Nous utilisons la fonction `do_plot` pour afficher l'image distordue.

```python
# préparer l'image et la figure
fig, ax2 = plt.subplots()
Z = get_image()

# distorsion de l'image
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
```
