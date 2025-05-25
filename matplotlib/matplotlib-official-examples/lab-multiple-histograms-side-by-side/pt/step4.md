# Plotar os histogramas

Agora que calculamos as quantidades necessárias para a plotagem, podemos criar nossos histogramas. Usaremos o método `barh` para plotar barras horizontais para cada histograma:

```python
# The bin_edges are the same for all of the histograms
bin_edges = np.linspace(hist_range[0], hist_range[1], number_of_bins + 1)
heights = np.diff(bin_edges)
centers = bin_edges[:-1] + heights / 2

# Cycle through and plot each histogram
fig, ax = plt.subplots()
for x_loc, binned_data in zip(x_locations, binned_data_sets):
    lefts = x_loc - 0.5 * binned_data
    ax.barh(centers, binned_data, height=heights, left=lefts)

ax.set_xticks(x_locations, labels)
ax.set_ylabel("Valores dos dados")
ax.set_xlabel("Conjuntos de dados")
```
