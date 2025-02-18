# 目盛りを調整する

ここでは、x 軸の目盛り（tick）を調整します。`ax1.xaxis.tick_top` を使用して最初のサブプロットの目盛りを上部に移動し、`ax1.tick_params(labeltop=False)` を使用して最初のサブプロットの目盛りラベルを削除し、2 番目のサブプロットの目盛りラベルは残します。

```python
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()
```
