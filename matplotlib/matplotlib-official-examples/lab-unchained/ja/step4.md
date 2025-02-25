# 範囲の設定と目盛りの削除

このステップでは、y軸の範囲を設定し、グラフから目盛りを削除します。

```python
# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 70)

# No ticks
ax.set_xticks([])
ax.set_yticks([])
```
