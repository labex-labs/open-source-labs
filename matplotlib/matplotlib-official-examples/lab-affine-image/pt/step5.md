# Realizar a Escala e Reflexão da Imagem

Nesta etapa, realizamos uma escala e reflexão da imagem usando a função `scale`. Passamos os fatores de escala e reflexão como entradas para a função `scale`. Usamos a função `do_plot` para exibir a imagem escalada e refletida.

```python
# prepare image and figure
fig, ax3 = plt.subplots()
Z = get_image()

# scale and reflection
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1, .5))
```
