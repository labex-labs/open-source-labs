# 创建数据

接下来，我们需要创建用于绘制线条的数据。我们将使用`numpy`创建一个包含`x`和`y`值的二维数组。

```python
x = np.arange(100)
ys = x[:50, np.newaxis] + x[np.newaxis, :]
```
