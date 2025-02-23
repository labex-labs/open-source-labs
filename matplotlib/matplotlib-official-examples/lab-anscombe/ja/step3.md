# サブプロット付きのグラフを作成する

ここでは、4 つのサブプロット付きのグラフを作成します。各サブプロットには、それぞれのデータセット用のものを用意します。また、すべてのサブプロットに対して x 軸と y 軸の範囲を同じに設定します。

```python
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 6),
                        gridspec_kw={'wspace': 0.08, 'hspace': 0.08})
axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(4, 8, 12))
```
