# Criando o Gráfico

Nesta etapa, criaremos o gráfico de contorno mascarado usando a função `contourf()`. Passamos os arrays `x`, `y` e `z` para esta função, juntamente com o argumento `corner_mask` definido como `True` ou `False`, dependendo do tipo de gráfico que queremos criar.

```python
corner_masks = [False, True]
fig, axs = plt.subplots(ncols=2)
for ax, corner_mask in zip(axs, corner_masks):
    cs = ax.contourf(x, y, z, corner_mask=corner_mask)
    ax.contour(cs, colors='k')
    ax.set_title(f'{corner_mask=}')

    # Plot grid.
    ax.grid(c='k', ls='-', alpha=0.3)

    # Indicate masked points with red circles.
    ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
```
