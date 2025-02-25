# 垂直線の追加

`axvline()` 関数を使用して垂直線を追加します。

```python
# y範囲全体にわたるx = 1の垂直線。
ax.axvline(x=1)
# y範囲の上半分にわたるx = 0の太い青の垂直線。
ax.axvline(x=0, ymin=0.75, linewidth=8, color='#1f77b4')
```
