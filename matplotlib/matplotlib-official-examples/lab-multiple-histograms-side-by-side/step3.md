# Compute quantities for plotting

Before we can create our histograms, we need to compute some quantities for plotting. We will compute the range of our datasets, the binned data sets, the maximum bin values, and the x-locations for each histogram:

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
