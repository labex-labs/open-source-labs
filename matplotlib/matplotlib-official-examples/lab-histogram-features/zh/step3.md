# 创建直方图

在这一步中，我们将使用 matplotlib 创建一个直方图。我们将把 bins 的数量设置为 50，并启用密度参数以对 bin 的高度进行归一化，使得直方图的积分等于 1。

```python
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=True)
```
