# グラフの作成

Matplotlib を使ってグラフを作成します。xdata と ydata を使って `DataDisplayDownsampler` クラスのインスタンス `d` を作成します。subplots 関数を使って figure と axis を作成します。線を接続して autoscale を False に設定します。表示範囲を変更するために接続し、x 軸の範囲を設定してグラフを表示します。

```python
d = DataDisplayDownsampler(xdata, ydata)
fig, ax = plt.subplots()
d.line, = ax.plot(xdata, ydata, 'o-')
ax.set_autoscale_on(False)
ax.callbacks.connect('xlim_changed', d.update)
ax.set_xlim(16, 365)
plt.show()
```
