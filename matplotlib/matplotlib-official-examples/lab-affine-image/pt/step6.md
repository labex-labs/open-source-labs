# Realizar Múltiplas Transformações

Nesta etapa, realizamos múltiplas transformações da imagem usando as funções `rotate_deg`, `skew_deg`, `scale` e `translate`. Passamos os parâmetros de transformação como entradas para as funções respectivas. Usamos a função `do_plot` para exibir a imagem transformada.

```python
# prepare image and figure
fig, ax4 = plt.subplots()
Z = get_image()

# everything and a translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1, .5).translate(.5, -1))
```
