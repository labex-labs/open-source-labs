# 定义数据

下一步是定义我们将在绘图中使用的数据。我们将使用 NumPy 的`arange`函数创建一个从 0 到 5、步长为 0.1 的数值数组。我们将把这个数组用作 x 轴。我们还将通过使用 NumPy 的指数函数和正弦函数来定义 y 轴。

```python
# 定义数据
t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.sin(2 * np.pi * t) + 1
```
