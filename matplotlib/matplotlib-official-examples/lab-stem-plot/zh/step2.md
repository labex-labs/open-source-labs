# 生成数据

接下来，我们需要生成一些数据用于茎叶图。我们将使用 Numpy 库创建两个数组。

```python
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
```
