# 플로팅을 위한 값 계산

히스토그램을 생성하기 전에, 플로팅을 위한 몇 가지 값을 계산해야 합니다. 데이터 세트의 범위, binning 된 데이터 세트, 최대 bin 값, 각 히스토그램의 x 위치를 계산합니다.

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
