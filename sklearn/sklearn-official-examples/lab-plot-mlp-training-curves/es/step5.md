# Trazar las curvas de aprendizaje para cada conjunto de datos

Finalmente, podemos trazar las curvas de aprendizaje para cada conjunto de datos usando la función plot_on_dataset. Crearemos una gráfica de 2x2 y trazaremos cada conjunto de datos en un eje separado.

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

for ax, data, name in zip(
    axes.ravel(), data_sets, ["iris", "digits", "circles", "moons"]
):
    plot_on_dataset(*data, ax=ax, name=name)

fig.legend(ax.get_lines(), labels, ncol=3, loc="upper center")
plt.show()
```
