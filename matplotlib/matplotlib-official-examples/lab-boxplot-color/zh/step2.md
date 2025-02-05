# 创建随机测试数据

接下来，我们将使用 `numpy` 库创建随机测试数据。我们将生成 3 组数据，每组数据具有不同的标准差。

```python
np.random.seed(19680801)
all_data = [np.random.normal(0, std, size=100) for std in range(1, 4)]
labels = ['x1', 'x2', 'x3']
```
