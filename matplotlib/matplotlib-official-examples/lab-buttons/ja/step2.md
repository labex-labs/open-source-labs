# 初期のグラフを設定する

次に、初期のグラフを設定します。`numpy`の`arange`関数を使って周波数 2Hz の正弦波を作成し、`matplotlib.pyplot`の`plot`関数を使ってプロットします。

```python
freqs = np.arange(2, 20, 3)
fig, ax = plt.subplots()
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = ax.plot(t, s, lw=2)
```
