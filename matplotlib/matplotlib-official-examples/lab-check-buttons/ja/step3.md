# プロットの作成

次に、`matplotlib`を使ってプロットを作成します。3 つのサイン波を同じグラフにプロットし、最初の波の可視性を`False`に設定します。なぜなら、最初は非表示にしておきたいからです。

```python
fig, ax = plt.subplots()
l0, = ax.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
l1, = ax.plot(t, s1, lw=2, color='red', label='2 Hz')
l2, = ax.plot(t, s2, lw=2, color='green', label='3 Hz')
fig.subplots_adjust(left=0.2)
```
