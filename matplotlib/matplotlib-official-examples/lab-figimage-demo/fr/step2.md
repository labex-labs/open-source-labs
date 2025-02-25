# Création de la figure et de l'image

Ensuite, nous créons la figure et l'image que nous voulons placer dedans. Dans cet exemple, nous créons un tableau de 100x100 de valeurs aléatoires et nous définissons les valeurs dans la moitié droite de l'image sur 1. Nous créons ensuite deux instances séparées de l'image, chacune avec une position et une opacité différentes.

```python
fig = plt.figure()
Z = np.arange(10000).reshape((100, 100))
Z[:, 50:] = 1

im1 = fig.figimage(Z, xo=50, yo=0, origin='lower')
im2 = fig.figimage(Z, xo=100, yo=100, alpha=.8, origin='lower')
```
