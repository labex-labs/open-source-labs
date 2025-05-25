# Iterar sobre a grade e plotar as imagens

Em seguida, iteramos sobre o objeto `grid` usando a função `zip` para iterar sobre os eixos e os arrays de imagem. Plotamos cada imagem em seu eixo correspondente usando a função `imshow`.

```python
for ax, im in zip(grid, [im1, im2, im3, im4]):
    ax.imshow(im)
```
