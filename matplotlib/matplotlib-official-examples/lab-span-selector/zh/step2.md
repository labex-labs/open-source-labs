# 创建示例数据

我们现在将使用 `numpy` 创建一些用于绘图的示例数据。

```python
# 为保证可重复性而固定随机数种子
np.random.seed(19680801)

x = np.arange(0.0, 5.0, 0.01)
y = np.sin(2 * np.pi * x) + 0.5 * np.random.randn(len(x))
```
