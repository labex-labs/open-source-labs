# 生成数据

接下来，我们将生成一些随机的二维数据用于直方图。我们将使用 NumPy 的 `random.rand()` 函数为 x 和 y 变量各生成 100 个随机值。

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 100) * 4
```
