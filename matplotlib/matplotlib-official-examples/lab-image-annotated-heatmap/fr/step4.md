# Exemples de cartes thermiques plus complexes

Dans ce qui suit, nous montrons la polyvalence des fonctions créées précédemment en les appliquant dans différents cas et en utilisant différents arguments.

```python
np.random.seed(19680801)

fig, ((ax, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 6))

# Reproduisez l'exemple ci-dessus avec une taille de police et une carte de couleur différentes.

im, _ = heatmap(récolte, légumes, fermiers, ax=ax, cmap="Wistia", cbarlabel="récolte [t/an]")
annotate_heatmap(im, valfmt="{x:.1f}", size=7)

# Parfois, même les données elles-mêmes sont catégorielles. Ici, nous utilisons un `matplotlib.colors.BoundaryNorm` pour classer les données et les utiliser pour colorier le tracé, mais également pour obtenir les étiquettes de classe à partir d'un tableau de classes.

data = np.random.randn(6, 6)
y = [f"Prod. {i}" for i in range(10, 70, 10)]
x = [f"Cycle {i}" for i in range(1, 7)]

qrates = list("ABCDEFG")
norm = matplotlib.colors.BoundaryNorm(np.linspace(-3.5, 3.5, 8), 7)
fmt = matplotlib.ticker.FuncFormatter(lambda x, pos: qrates[::-1][norm(x)])

im, _ = heatmap(data, y, x, ax=ax3, cmap=mpl.colormaps["PiYG"].resampled(7), norm=norm, cbar_kw=dict(ticks=np.arange(-3, 4), format=fmt), cbarlabel="Note de qualité")
annotate_heatmap(im, valfmt=fmt, size=9, fontweight="bold", threshold=-1, textcolors=("rouge", "noir"))

# Nous pouvons tracer agréablement une matrice de corrélation. Puisque celle-ci est limitée entre -1 et 1, nous utilisons ces valeurs comme vmin et vmax.

corr_matrix = np.corrcoef(récolte)
im, _ = heatmap(corr_matrix, légumes, légumes, ax=ax4, cmap="PuOr", vmin=-1, vmax=1, cbarlabel="coeff. de corrélation")
annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)

plt.tight_layout()
plt.show()
```
