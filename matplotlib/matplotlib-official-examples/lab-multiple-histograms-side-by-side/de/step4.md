# Die Histogramme plotten

Jetzt, nachdem wir die erforderlichen Größen für das Plotten berechnet haben, können wir unsere Histogramme erstellen. Wir werden die `barh`-Methode verwenden, um horizontale Balken für jedes Histogramm zu plotten:

```python
# Die Bin-Umrandungen sind für alle Histogramme gleich
bin_edges = np.linspace(hist_range[0], hist_range[1], number_of_bins + 1)
heights = np.diff(bin_edges)
centers = bin_edges[:-1] + heights / 2

# Gehen Sie durch und plotten Sie jedes Histogramm
fig, ax = plt.subplots()
for x_loc, binned_data in zip(x_locations, binned_data_sets):
    lefts = x_loc - 0.5 * binned_data
    ax.barh(centers, binned_data, height=heights, left=lefts)

ax.set_xticks(x_locations, labels)
ax.set_ylabel("Datenwerte")
ax.set_xlabel("Datensätze")
```
