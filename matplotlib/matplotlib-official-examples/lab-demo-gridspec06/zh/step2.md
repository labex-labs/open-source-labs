# 创建数据

在这一步中，我们将创建一些用于绘图的数据。我们将使用`squiggle_xy`函数来生成一些具有不同频率的正弦和余弦波。

```python
def squiggle_xy(a, b, c, d):
    i = np.arange(0.0, 2*np.pi, 0.05)
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)
```
