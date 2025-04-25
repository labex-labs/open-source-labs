# `GridSpec` を使ってサブプロットを生成する

このステップでは、`GridSpec` を使ってサブプロットを生成します。2 行 2 列の図を作成します。また、サブプロットの相対サイズを制御するために `width_ratios` と `height_ratios` を指定します。

```python
fig = plt.figure()
gs = GridSpec(2, 2, width_ratios=[1, 2], height_ratios=[4, 1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
```
