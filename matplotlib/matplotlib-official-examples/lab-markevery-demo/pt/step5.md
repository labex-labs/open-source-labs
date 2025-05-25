# Criar Gráficos Polares

Finalmente, criamos um conjunto de subplots para mostrar como `markevery` se comporta em gráficos polares. Notamos que o comportamento é semelhante ao das escalas lineares.

```python
# create polar plots
r = np.linspace(0, 3.0, 200)
theta = 2 * np.pi * r

fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained',
                        subplot_kw={'projection': 'polar'})
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(theta, r, 'o', ls='-', ms=4, markevery=markevery)
```
