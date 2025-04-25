# グラフとサブプロットを作成する

このステップでは、累積分布用の 2 つのサブプロット付きのグラフを作成します。また、グラフのサイズを 9x4 に設定します。

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```
