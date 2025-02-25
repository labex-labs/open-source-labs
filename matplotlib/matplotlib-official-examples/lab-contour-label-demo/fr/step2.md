# Créer des étiquettes de contour avec des formatteurs de niveau personnalisés

Nous allons maintenant créer des étiquettes de contour avec des formatteurs de niveau personnalisés. Cela nous permettra de formater les étiquettes d'une manière spécifique. Dans ce cas, nous allons supprimer les zéros terminaux et ajouter un signe pourcentage.

```python
def fmt(x):
    s = f"{x:.1f}"
    if s.endswith("0"):
        s = f"{x:.0f}"
    return rf"{s} \%" if plt.rcParams["text.usetex"] else f"{s} %"

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10)
```
