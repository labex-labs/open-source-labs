# Вычисляем величины для построения

Прежде чем мы сможем создать наши гистограммы, нам нужно вычислить некоторые величины для построения. Мы вычислим диапазон наших наборов данных, сгруппированные наборы данных, максимальные значения интервалов и расположения по оси x для каждой гистограммы:

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
