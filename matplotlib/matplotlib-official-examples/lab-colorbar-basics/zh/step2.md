# 生成数据

我们使用 `numpy` 的 `mgrid` 函数生成一些用于绘图的示例数据。

```python
# 设置一些通用数据
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))
```
