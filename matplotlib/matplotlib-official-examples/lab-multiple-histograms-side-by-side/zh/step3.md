# 计算绘图所需的量

在创建直方图之前，我们需要计算一些用于绘图的量。我们将计算数据集的范围、装箱后的数据集、每个箱子的最大值以及每个直方图的x轴位置：

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
