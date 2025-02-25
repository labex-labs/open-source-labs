# Coordonnées centrées

Souvent, un utilisateur veut passer _X_ et _Y_ de la même taille que _Z_ à `.axes.Axes.pcolormesh`. Cela est également autorisé si `shading='auto'` est passé (valeur par défaut définie par :rc:`pcolor.shading`). Avant Matplotlib 3.3, `shading='flat'` supprimait la dernière colonne et la dernière ligne de _Z_, mais maintenant cela génère une erreur. Si c'est vraiment ce que vous voulez, alors supprimez simplement la dernière ligne et la dernière colonne de Z manuellement :

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(10)  # len = 10
y = np.arange(6)  # len = 6
X, Y = np.meshgrid(x, y)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
axs[0].pcolormesh(X, Y, Z, vmin=np.min(Z), vmax=np.max(Z), shading='auto')
axs[0].set_title("shading='auto' = 'nearest'")
axs[1].pcolormesh(X, Y, Z[:-1, :-1], vmin=np.min(Z), vmax=np.max(Z),
                  shading='flat')
axs[1].set_title("shading='flat'")
```
