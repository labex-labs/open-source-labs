# Realizar la escala y reflexión de la imagen

En este paso, realizamos una escala y reflexión de la imagen utilizando la función `scale`. Pasamos los factores de escala y reflexión como entradas a la función `scale`. Utilizamos la función `do_plot` para mostrar la imagen escalada y reflejada.

```python
# prepare image and figure
fig, ax3 = plt.subplots()
Z = get_image()

# scale and reflection
do_plot(ax3, Z, mtransforms.Affine2D().scale(-1,.5))
```
