# 创建一个随机矩阵

接下来，我们将使用 numpy 创建一个随机矩阵。我们将使用 `rand` 方法创建一个 5x3 的矩阵，其随机值介于 0 和 1 之间。我们还将设置一个随机种子以确保结果的可重复性。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

X = 10*np.random.rand(5, 3)
```
