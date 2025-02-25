# グラフとサブプロットを作成する

このステップでは、累積分布用の2つのサブプロット付きのグラフを作成します。また、グラフのサイズを9x4に設定します。

```python
fig = plt.figure(figsize=(9, 4), layout="constrained")
axs = fig.subplots(1, 2, sharex=True, sharey=True)
```
