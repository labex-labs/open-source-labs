# Créer des graphiques polaires

Enfin, nous créons un ensemble de sous-graphiques pour montrer le comportement de `markevery` sur des graphiques polaires. Nous notons que le comportement est similaire à celui sur les échelles linéaires.

```python
# créer des graphiques polaires
r = np.linspace(0, 3.0, 200)
theta = 2 * np.pi * r

fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained',
                        subplot_kw={'projection': 'polar'})
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(theta, r, 'o', ls='-', ms=4, markevery=markevery)
```
