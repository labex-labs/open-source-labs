# Créez des contours remplis avec des trous

Plusieurs lignes de contour remplies peuvent être spécifiées dans une seule liste de sommets de polygone, ainsi qu'une liste de types de sommets (types de code) comme décrit dans la classe Path. Cela est particulièrement utile pour les polygones avec des trous.

```python
fig, ax = plt.subplots()
filled01 = [[[0, 0], [3, 0], [3, 3], [0, 3], [1, 1], [1, 2], [2, 2], [2, 1]]]
M = Path.MOVETO
L = Path.LINETO
kinds01 = [[M, L, L, L, M, L, L, L]]
cs = ContourSet(ax, [0, 1], [filled01], [kinds01], filled=True)
cbar = fig.colorbar(cs)

ax.set(xlim=(-0.5, 3.5), ylim=(-0.5, 3.5),
       title='Contours remplis spécifiés par l\'utilisateur avec des trous')
```
