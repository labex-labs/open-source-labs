# 创建数据

接下来，我们将创建一些要绘制的数据。我们将使用 `numpy` 库来创建一个正弦波。

```python
x = np.arange(0, 10, 0.005)
y = np.exp(-x/2.) * np.sin(2*np.pi*x)
```
