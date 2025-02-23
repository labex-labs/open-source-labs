# Effectuer une mise à l'échelle et une réflexion de l'image

Dans cette étape, nous effectuons une mise à l'échelle et une réflexion de l'image à l'aide de la fonction `scale`. Nous passons les facteurs de mise à l'échelle et de réflexion en tant qu'entrées à la fonction `scale`. Nous utilisons la fonction `do_plot` pour afficher l'image mise à l'échelle et réfléchie.

```python
# préparer l'image et la figure
fig, ax3 = plt.subplots()
Z = get_image()

# mise à l'échelle et réflexion
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1,.5))
```
