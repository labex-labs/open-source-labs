# 領域を塗りつぶす

正弦波が正と負のときに、それぞれ水平線の上と下の領域を塗りつぶすために`fill_between`を使用します。

```python
ax.fill_between(t, 1, where=s > 0, facecolor='green', alpha=.5)
ax.fill_between(t, -1, where=s < 0, facecolor='red', alpha=.5)
```
