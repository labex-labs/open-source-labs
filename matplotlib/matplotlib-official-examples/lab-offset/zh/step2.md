# 创建数据

接下来，我们创建将在绘图中使用的数据。在这个例子中，我们将使用 NumPy 来生成数据。

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
```
