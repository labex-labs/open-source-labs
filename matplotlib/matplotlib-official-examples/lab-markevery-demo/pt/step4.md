# Criar Gráficos Zoomados

Criamos outro conjunto de subplots, desta vez para mostrar como `markevery` se comporta em gráficos zoomados. Notamos que a subamostragem baseada em inteiros seleciona pontos dos dados subjacentes e é independente da visualização, enquanto a subamostragem baseada em float está relacionada à diagonal dos eixos (Axes) e altera a faixa de dados exibida.

```python
# create zoomed plots
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
    ax.set_xlim((6, 6.7))
    ax.set_ylim((1.1, 1.7))
```
