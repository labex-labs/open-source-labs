# 目盛りとグリッド線の zorder の設定

目盛りとグリッド線の `zorder` を設定するには、`set_axisbelow()` メソッドまたは `axes.axisbelow` パラメータを使用します。

```python
ax = plt.axes()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
```
