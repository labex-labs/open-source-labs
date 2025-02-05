# 生成条形图的数据

现在我们将生成条形图的数据。我们将创建四组数据，每组有20个值。我们将使用NumPy的 `arange()` 方法创建一个包含20个值的数组，并使用NumPy的 `random.rand()` 方法为每组数据生成随机值。

```python
colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)
```
