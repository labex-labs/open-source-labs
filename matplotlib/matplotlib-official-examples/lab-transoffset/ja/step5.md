# 極座標グラフの作成

ここでは、`matplotlib.pyplot` の `polar` 関数を使用して極座標グラフを作成します。

```python
ax = plt.subplot(2, 1, 2, projection='polar')

# Plot the data
for x, y in zip(xs, ys):
    plt.polar(x, y, 'ro')
```
