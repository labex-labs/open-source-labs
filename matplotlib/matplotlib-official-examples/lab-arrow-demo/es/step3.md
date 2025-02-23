# Personalizar el diagrama de flechas

El tercer paso es personalizar el diagrama de flechas. Podemos cambiar la propiedad de la flecha para mostrar utilizando el parámetro `display`. También podemos cambiar la forma de la flecha utilizando el parámetro `shape`. Podemos ajustar el ancho y la separación de las flechas utilizando los parámetros `max_arrow_width` y `arrow_sep`, respectivamente. Podemos cambiar la transparencia de las flechas utilizando el parámetro `alpha`. También podemos cambiar el color de la etiqueta utilizando el parámetro `labelcolor`.

```python
# Trazar el diagrama de flechas con personalizaciones
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size, shape='full', max_arrow_width=0.05,
        arrow_sep=0.03, alpha=0.7, labelcolor='white')

plt.show()
```
