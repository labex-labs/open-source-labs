# Ajout de texte au graphique

Nous pouvons ajouter du texte au graphique à l'aide de la fonction `ax.text()`. Cette fonction prend trois arguments : la coordonnée x, la coordonnée y et la chaîne de caractères du texte. Nous pouvons personnaliser le style du texte à l'aide des arguments `style`, `bbox` et `fontsize`.

```python
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor':'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'Unicode: Institut f\374r Festk\366rperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
```
