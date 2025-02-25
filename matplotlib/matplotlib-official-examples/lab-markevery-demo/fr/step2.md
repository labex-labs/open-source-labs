# Créer des graphiques avec des échelles linéaires

Ensuite, nous créons un ensemble de sous-graphiques pour montrer le comportement de `markevery` avec des échelles linéaires. Nous parcourons la liste `cases` et traçons chaque cas sur un sous-graphique séparé. Nous utilisons le paramètre `markevery` pour spécifier les points de données à marquer.

```python
# créer des graphiques avec des échelles linéaires
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
