# Representar los histogramas

Ahora que hemos calculado las cantidades necesarias para la representación gráfica, podemos crear nuestros histogramas. Usaremos el método `barh` para representar barras horizontales para cada histograma:

```python
# Los bordes de los intervalos son los mismos para todos los histogramas
bin_edges = np.linspace(hist_range[0], hist_range[1], number_of_bins + 1)
heights = np.diff(bin_edges)
centers = bin_edges[:-1] + heights / 2

# Recorrer y representar cada histograma
fig, ax = plt.subplots()
for x_loc, binned_data in zip(x_locations, binned_data_sets):
    lefts = x_loc - 0.5 * binned_data
    ax.barh(centers, binned_data, height=heights, left=lefts)

ax.set_xticks(x_locations, labels)
ax.set_ylabel("Valores de datos")
ax.set_xlabel("Conjuntos de datos")
```
