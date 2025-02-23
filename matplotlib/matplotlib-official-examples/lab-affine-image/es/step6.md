# Realizar múltiples transformaciones

En este paso, realizamos múltiples transformaciones de la imagen utilizando las funciones `rotate_deg`, `skew_deg`, `scale` y `translate`. Pasamos los parámetros de transformación como entradas a las respectivas funciones. Utilizamos la función `do_plot` para mostrar la imagen transformada.

```python
# prepare image and figure
fig, ax4 = plt.subplots()
Z = get_image()

# everything and a translation
do_plot(ax4, Z, mtransforms.Affine2D().
        rotate_deg(30).skew_deg(30, 15).scale(-1,.5).translate(.5, -1))
```
