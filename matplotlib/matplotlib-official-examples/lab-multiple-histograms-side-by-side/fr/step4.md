# Tracez les histogrammes

Maintenant que nous avons calculé les quantités nécessaires pour le tracé, nous pouvons créer nos histogrammes. Nous utiliserons la méthode `barh` pour tracer des barres horizontales pour chaque histogramme :

```python
# Les limites des bins sont les mêmes pour tous les histogrammes
bin_edges = np.linspace(hist_range[0], hist_range[1], number_of_bins + 1)
heights = np.diff(bin_edges)
centers = bin_edges[:-1] + heights / 2

# Parcourez et tracez chaque histogramme
fig, ax = plt.subplots()
for x_loc, binned_data in zip(x_locations, binned_data_sets):
    lefts = x_loc - 0.5 * binned_data
    ax.barh(centers, binned_data, height=heights, left=lefts)

ax.set_xticks(x_locations, labels)
ax.set_ylabel("Valeurs des données")
ax.set_xlabel("Ensembles de données")
```
