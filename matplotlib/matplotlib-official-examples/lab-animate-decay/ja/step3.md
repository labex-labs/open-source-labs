# グラフを設定する

次に、グラフを設定する必要があります。Matplotlibの`subplots()`関数を使って、グラフと軸のオブジェクトを作成します。また、サイン波を表す線のオブジェクトも作成します。

```python
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
```
