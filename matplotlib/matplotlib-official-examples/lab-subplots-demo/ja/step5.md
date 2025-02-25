# 極座標軸

`subplots()`関数に`projection='polar'`パラメータを渡すことで、極座標の`Axes`のグリッドを作成できます。

```python
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
ax1.plot(x, y)
ax2.plot(x, y ** 2)
```
