# 垂直線を追加する

このステップでは、グラフに垂直線を追加します。Matplotlib の `vlines` 関数を使って垂直線を描画します。また、`transform` パラメータを使って y 座標を 0 から 1 までにスケーリングするように設定します。x = 1 と x = 2 のところに 2 本の垂直線を描画します。

```python
# Add vertical lines
vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')
```
