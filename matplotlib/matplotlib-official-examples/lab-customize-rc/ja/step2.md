# デフォルトパラメータをカスタマイズする

特定のグラフのデフォルトパラメータをカスタマイズするには、再び `rcParams.update()` メソッドを使用できます。今回は、そのグラフに設定したいパラメータ名と値の辞書を渡します。以下は、特定のグラフにいくつかのデフォルトパラメータを設定する例です：

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.weight": "bold",
    "xtick.major.size": 5,
    "xtick.major.pad": 7,
    "xtick.labelsize": 15,
    "grid.color": "0.5",
    "grid.linestyle": "-",
    "grid.linewidth": 5,
    "lines.linewidth": 2,
    "lines.color": "g",
})
```
