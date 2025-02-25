# 2次元ヒストグラムを描画する

2次元ヒストグラムを描画するには、ヒストグラムの各軸に対応する同じ長さの2つのベクトルだけが必要です。

```python
fig, ax = plt.subplots(tight_layout=True)
hist = ax.hist2d(dist1, dist2)

plt.show()
```
