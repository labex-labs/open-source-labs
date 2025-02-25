# Größen für das Plotten berechnen

Bevor wir unsere Histogramme erstellen können, müssen wir einige Größen für das Plotten berechnen. Wir werden den Wertebereich unserer Datensätze, die gruppierten Datensätze, die maximalen Bin-Werte und die x-Positionen für jedes Histogramm berechnen:

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
