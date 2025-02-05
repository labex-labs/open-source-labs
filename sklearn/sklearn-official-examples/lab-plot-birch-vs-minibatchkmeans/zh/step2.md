# 生成数据集

下一步是生成数据集，以便对MiniBatchKMeans和BIRCH进行比较。我们将使用matplotlib默认提供的所有颜色。

```python
# 为数据集生成中心点，使其形成一个10X10的网格。
xx = np.linspace(-22, 22, 10)
yy = np.linspace(-22, 22, 10)
xx, yy = np.meshgrid(xx, yy)
n_centers = np.hstack((np.ravel(xx)[:, np.newaxis], np.ravel(yy)[:, np.newaxis]))

# 生成数据集，以便对MiniBatchKMeans和BIRCH进行比较。
X, y = make_blobs(n_samples=25000, centers=n_centers, random_state=0)

# 使用matplotlib默认提供的所有颜色。
colors_ = cycle(colors.cnames.keys())
```
