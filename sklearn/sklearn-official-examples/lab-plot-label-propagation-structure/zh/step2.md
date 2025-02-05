# 生成数据集

接下来，我们使用 `make_circles` 生成一个包含两个同心圆的数据集。我们为数据集分配标签，使得除了分别属于外圆和内圆的两个样本外，所有样本都是未知的。

```python
n_samples = 200
X, y = make_circles(n_samples=n_samples, shuffle=False)
outer, inner = 0, 1
labels = np.full(n_samples, -1.0)
labels[0] = outer
labels[-1] = inner
```
