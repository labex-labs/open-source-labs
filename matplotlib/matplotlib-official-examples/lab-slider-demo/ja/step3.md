# 初期グラフの作成

次に、サイン波の初期グラフを作成します。振幅と周波数の初期パラメータを定義し、それらのパラメータを使ってサイン波をプロットします。

```python
t = np.linspace(0, 1, 1000)
init_amplitude = 5
init_frequency = 3

fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
```
