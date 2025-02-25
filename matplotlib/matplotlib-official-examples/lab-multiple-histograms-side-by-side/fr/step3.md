# Calculez les quantités pour le tracé

Avant de pouvoir créer nos histogrammes, nous devons calculer certaines quantités pour le tracé. Nous allons calculer la plage de nos ensembles de données, les ensembles de données regroupés par bins, les valeurs maximales de chaque bin et les emplacements x pour chaque histogramme :

```python
hist_range = (np.min(data_sets), np.max(data_sets))
number_of_bins = 20
binned_data_sets = [
    np.histogram(d, range=hist_range, bins=number_of_bins)[0]
    for d in data_sets
]
binned_maximums = np.max(binned_data_sets, axis=1)
x_locations = np.arange(0, sum(binned_maximums), np.max(binned_maximums))
```
