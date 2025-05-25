# Realizar a Rotação da Imagem

Nesta etapa, realizamos uma rotação da imagem usando a função `rotate_deg`. Passamos o ângulo de rotação como entrada para a função `rotate_deg`. Usamos a função `do_plot` para exibir a imagem rotacionada.

```python
# prepare image and figure
fig, ax1 = plt.subplots()
Z = get_image()

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))
```
