# Criar Gráficos com Escalas Lineares

Em seguida, criamos um conjunto de subplots para mostrar como `markevery` se comporta com escalas lineares. Iteramos pela lista `cases` e plotamos cada caso em um subplot separado. Usamos o parâmetro `markevery` para especificar quais pontos de dados marcar.

```python
# create plots with linear scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
