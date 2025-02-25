# 水平線を追加する

このステップでは、グラフに水平線を追加します。Matplotlib の `hlines` 関数を使って水平線を描画します。y = 0.5、y = 2.5、および y = 4.5 のところに水平線を描画します。

```python
# Add horizontal lines
hax.plot(s + nse, t, '^')
hax.hlines(t, [0], s, lw=2)
hax.set_xlabel('time (s)')
hax.set_title('Horizontal lines demo')
```
