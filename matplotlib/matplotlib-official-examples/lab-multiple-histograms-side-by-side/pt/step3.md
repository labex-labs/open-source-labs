# Calcular as quantidades para plotagem

Antes de podermos criar nossos histogramas, precisamos calcular algumas quantidades para plotagem. Calcularemos o intervalo de nossos conjuntos de dados, os conjuntos de dados binados, os valores máximos dos bins e as localizações x para cada histograma:

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
