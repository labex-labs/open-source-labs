# グラフを作成する

次に、Matplotlibを使ってグラフを作成します。この例では、コサイン関数を値の範囲にわたってプロットします。

```python
fig, ax = plt.subplots()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
```
