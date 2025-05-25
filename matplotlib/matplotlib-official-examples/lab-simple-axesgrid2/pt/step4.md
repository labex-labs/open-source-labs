# Exibir imagens no ImageGrid

Finalmente, exibimos as imagens no ImageGrid usando a função `imshow` e a função `zip` para iterar pelos eixos na grade.

```python
for ax, im in zip(grid, [im1, im2, im3]):
    ax.imshow(im, origin="lower", vmin=vmin, vmax=vmax)

plt.show()
```
