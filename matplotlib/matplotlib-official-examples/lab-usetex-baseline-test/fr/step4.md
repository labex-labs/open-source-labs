# Ajoutez des chaînes de test au graphique

Nous allons ajouter quatre chaînes de test à chaque sous-graphique, chacun avec un style et une position différents. Nous utiliserons la méthode `text()` pour ajouter le texte aux sous-graphiques.

```python
test_strings = ["lg", r"$\frac{1}{2}\pi$", r"$p^{3^A}$", r"$p_{3_2}$"]
for ax, usetex in zip(axs, [False, True]):
    ax.axvline(0, color="r")
    for i, s in enumerate(test_strings):
        ax.axhline(i, color="r")
        ax.text(0., 3 - i, s,
                usetex=usetex,
                verticalalignment="baseline",
                size=50,
                bbox=dict(pad=0, ec="k", fc="none"))
```
