# 创建一些模拟数据

接下来，我们将创建一些模拟数据用于绘制图表。我们将使用 `numpy.arange` 创建一个值数组，其范围从 0.01 到 10.0，步长为 0.01。然后，我们将使用 `numpy.exp` 和 `numpy.sin` 创建两组数据。

```python
# 创建一些模拟数据
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
```
