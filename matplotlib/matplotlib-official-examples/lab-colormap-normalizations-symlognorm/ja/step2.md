# 合成データを作成する

このステップでは、一つが負でもう一つが正の2つの山を持つ合成データセットを作成します。正の山の振幅は負の山の8倍です。その後、データを可視化するために`SymLogNorm`を適用します。

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
