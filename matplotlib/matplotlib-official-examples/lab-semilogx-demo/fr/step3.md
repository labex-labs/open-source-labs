# Créer un graphique et définir l'échelle logarithmique pour l'axe x

Nous créons un objet figure et axes à l'aide de la méthode `subplots()`. Nous traçons ensuite la fonction de décroissance exponentielle à l'aide de la méthode `semilogx()` et définissons l'échelle de l'axe x sur une échelle logarithmique à l'aide de la méthode `set_xscale()`. Nous ajoutons également une grille au graphique à l'aide de la méthode `grid()`.

```python
fig, ax = plt.subplots()

ax.semilogx(t, np.exp(-t / 5.0))
ax.set_xscale('log')
ax.grid()
```
