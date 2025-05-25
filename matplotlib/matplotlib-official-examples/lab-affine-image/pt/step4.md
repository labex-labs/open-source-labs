# Realizar a Distorção da Imagem (Skew)

Nesta etapa, realizamos uma distorção (skew) da imagem usando a função `skew_deg`. Passamos os ângulos de distorção como entradas para a função `skew_deg`. Usamos a função `do_plot` para exibir a imagem distorcida.

```python
# prepare image and figure
fig, ax2 = plt.subplots()
Z = get_image()

# image skew
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
```
