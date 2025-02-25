# グラフと軸を作成する

このステップでは、グラフ用のグラフと軸を作成します。また、スライダー用のスペースを確保するために軸の位置を調整します。

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.25)
l, = ax.plot(t, s, lw=2)

ax_freq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_amp = fig.add_axes([0.25, 0.15, 0.65, 0.03])
```
