# サブプロットの周りと間の間隔を制御する

このステップでは、`GridSpec` を使ってサブプロットの周りと間の間隔を制御します。3 行 3 列のグリッドスペックを 2 つ持つ図を作成します。間隔を制御するために `left`、`right`、`bottom`、`top`、`wspace`、および `hspace` パラメータを指定します。

```python
fig = plt.figure()
gs1 = GridSpec(3, 3, left=0.05, right=0.48, wspace=0.05)
ax1 = fig.add_subplot(gs1[:-1, :])
ax2 = fig.add_subplot(gs1[-1, :-1])
ax3 = fig.add_subplot(gs1[-1, -1])

gs2 = GridSpec(3, 3, left=0.55, right=0.98, hspace=0.05)
ax4 = fig.add_subplot(gs2[:, :-1])
ax5 = fig.add_subplot(gs2[:-1, -1])
ax6 = fig.add_subplot(gs2[-1, -1])
```
