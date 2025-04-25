# 線と凡例を作成する

Matplotlib を使って 2 つの線と凡例を作成します。

```python
line1, = ax.plot(t, y1, lw=2, label='1 Hz')
line2, = ax.plot(t, y2, lw=2, label='2 Hz')
leg = ax.legend(fancybox=True, shadow=True)
```
