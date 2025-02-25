# Calcular cantidades para la representación gráfica

Antes de poder crear nuestros histogramas, necesitamos calcular algunas cantidades para la representación gráfica. Calcularemos el rango de nuestros conjuntos de datos, los conjuntos de datos agrupados en intervalos, los valores máximos de los intervalos y las ubicaciones en el eje x para cada histograma:

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
