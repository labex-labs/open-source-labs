# Créer des graphiques avec des échelles logarithmiques

Nous répétons l'étape précédente, mais cette fois avec des échelles logarithmiques. Nous notons que l'échelle logarithmique provoque une asymétrie visuelle dans la distance entre les marqueurs pour un sous-échantillonnage basé sur des entiers, tandis que le sous-échantillonnage basé sur des fractions crée des distributions uniformes.

```python
# créer des graphiques avec des échelles logarithmiques
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
