# 生成数据

我们将使用 Numpy 库中的 `linspace` 方法来生成动画所需的数据。我们将生成两组数据，x 和 y，然后对 y 数据进行重塑以创建一个二维数组。

```python
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
```
