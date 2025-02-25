# サブプロットの作成

色付けされた線分を表示するためにサブプロットを作成します。`matplotlib.pyplot` の `subplots` 関数を使って、2x1 のサブプロットのグリッドを作成し、`sharex` および `sharey` パラメータを使ってサブプロット間で x 軸と y 軸を共有します。

```python
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])
```
