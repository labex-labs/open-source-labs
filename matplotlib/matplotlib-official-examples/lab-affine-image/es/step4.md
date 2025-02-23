# Realizar la inclinación de la imagen

En este paso, realizamos una inclinación de la imagen utilizando la función `skew_deg`. Pasamos los ángulos de inclinación como entradas a la función `skew_deg`. Utilizamos la función `do_plot` para mostrar la imagen inclinada.

```python
# prepare image and figure
fig, ax2 = plt.subplots()
Z = get_image()

# image skew
do_plot(ax2, Z, mtransforms.Affine2D().skew_deg(30, 15))
```
