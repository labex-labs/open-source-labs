# ボタンコールバック関数を作成する

次に、`Next`と`Previous`のボタン用の 2 つのコールバック関数を作成します。これらの関数は、異なる周波数の新しい正弦波でグラフを更新します。

```python
class Index:
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

callback = Index()
```
