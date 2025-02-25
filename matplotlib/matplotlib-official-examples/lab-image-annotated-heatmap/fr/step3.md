# Application de la fonction

Maintenant que nous avons les fonctions, nous pouvons les utiliser pour créer une carte thermique avec des annotations. Nous créons un nouvel ensemble de données, donnons des arguments supplémentaires à `imshow`, utilisons un format entier pour les annotations et fournissons quelques couleurs. Nous masquons également les éléments diagonaux (qui sont tous égaux à 1) en utilisant un `matplotlib.ticker.FuncFormatter`.

```python
data = np.random.randint(2, 100, size=(7, 7))
y = [f"Livre {i}" for i in range(1, 8)]
x = [f"Boutique {i}" for i in list("ABCDEFG")]

fig, ax = plt.subplots()
im, _ = heatmap(data, y, x, ax=ax, vmin=0, cmap="magma_r", cbarlabel="exemplaires vendus hebdomadaires")
annotate_heatmap(im, valfmt="{x:d}", size=7, threshold=20, textcolors=("rouge", "blanc"))

def func(x, pos):
    return f"{x:.2f}".replace("0.", ".").replace("1.00", "")

annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)
```
