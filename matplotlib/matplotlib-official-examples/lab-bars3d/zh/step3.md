# 生成条形图的数据

现在我们将生成条形图的数据。我们将创建四组数据，每组有 20 个值。我们将使用 NumPy 的 `arange()` 方法创建一个包含 20 个值的数组，并使用 NumPy 的 `random.rand()` 方法为每组数据生成随机值。

```python
colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)
```
