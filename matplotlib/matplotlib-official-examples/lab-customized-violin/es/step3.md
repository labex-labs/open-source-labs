# Personalizar la apariencia del diagrama de violín

Ahora personalizaremos la apariencia del diagrama de violín. Primero, limitaremos lo que Matplotlib dibuja estableciendo los argumentos `showmeans`, `showmedians` y `showextrema` en `False`. Luego, cambiaremos el color y la opacidad de los cuerpos del violín utilizando los métodos `set_facecolor` y `set_alpha`. Finalmente, agregaremos una representación simplificada de un diagrama de caja encima del diagrama de violín, utilizando la función `percentile` de NumPy para calcular los cuartiles, la mediana y las bigotes.

```python
# customize violin plot appearance
fig, ax2 = plt.subplots()
ax2.set_title('Customized Violin Plot')
ax2.set_ylabel('Observed Values')

# create violin plot
parts = ax2.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)

# customize violin bodies
for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

# add box plot
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax2.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)
```
