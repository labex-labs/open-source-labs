# 極座標バーチャートを作成する

`projection='polar'` パラメータを使用して極座標バーチャートを作成します。

```python
ax = plt.subplot(projection='polar')
ax.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.5)
```
