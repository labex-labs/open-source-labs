# Ajouter les étiquettes d'axe et les étiquettes d'échelonnage

Ajoutez les étiquettes des axes x et y à l'aide de `figtext`. Masquez les spines supérieure et droite à l'aide de `spines`. Réglez le positionnement et les étiquettes d'échelonnage personnalisées à l'aide de `set_xticks` et `set_yticks`.

```python
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([a, b], labels=['$a$', '$b$'])
ax.set_yticks([])
```
