# Adicionar um gráfico de inserção (inset plot)

Nesta etapa, adicionaremos um gráfico de inserção ao gráfico principal. Este gráfico de inserção mostrará uma região ampliada do gráfico principal.

```python
# inset axes....
x1, x2, y1, y2 = -1.5, -0.9, -2.5, -1.9  # subregion of the original image
axins = ax.inset_axes(
    [0.5, 0.5, 0.47, 0.47],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.imshow(Z2, extent=extent, origin="lower")
```
