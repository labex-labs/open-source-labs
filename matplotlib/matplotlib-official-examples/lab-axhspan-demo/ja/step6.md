# 垂直線の追加

`axvline()` 関数を使用して垂直線を追加します。

```python
# y 範囲全体にわたる x = 1 の垂直線。
ax.axvline(x=1)
# y 範囲の上半分にわたる x = 0 の太い青の垂直線。
ax.axvline(x=0, ymin=0.75, linewidth=8, color='#1f77b4')
```
