# 3Dのステムプロットを作成する

このステップでは、Matplotlibの`stem`関数を使って3Dのステムプロットを作成します。`stem`関数にx座標、y座標、z座標を引数として渡します。

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```
