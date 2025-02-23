# Realizar la rotación de la imagen

En este paso, realizamos una rotación de la imagen utilizando la función `rotate_deg`. Pasamos el ángulo de rotación como entrada a la función `rotate_deg`. Utilizamos la función `do_plot` para mostrar la imagen rotada.

```python
# prepare image and figure
fig, ax1 = plt.subplots()
Z = get_image()

# image rotation
do_plot(ax1, Z, mtransforms.Affine2D().rotate_deg(30))
```
