# Créer des graphiques agrandis

Nous créons un autre ensemble de sous-graphiques, cette fois pour montrer le comportement de `markevery` sur des graphiques agrandis. Nous notons que le sous-échantillonnage basé sur des entiers sélectionne des points dans les données sous-jacentes et est indépendant de la vue, tandis que le sous-échantillonnage basé sur des flottants est lié à la diagonale des axes et change la plage de données affichée.

```python
# créer des graphiques agrandis
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
    ax.set_xlim((6, 6.7))
    ax.set_ylim((1.1, 1.7))
```
