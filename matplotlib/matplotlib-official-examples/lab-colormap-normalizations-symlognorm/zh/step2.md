# 创建合成数据

在这一步中，我们将创建一个由两个波峰组成的合成数据集，一个为负波峰，一个为正波峰，正波峰的幅度是负波峰的八倍。然后我们将应用`SymLogNorm`来可视化数据。

```python
def rbf(x, y):
    return 1.0 / (1 + 5 * ((x ** 2) + (y ** 2)))

N = 200
gain = 8
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z1 = rbf(X + 0.5, Y + 0.5)
Z2 = rbf(X - 0.5, Y - 0.5)
Z = gain * Z1 - Z2

shadeopts = {'cmap': 'PRGn','shading': 'gouraud'}
colormap = 'PRGn'
lnrwidth = 0.5
```
