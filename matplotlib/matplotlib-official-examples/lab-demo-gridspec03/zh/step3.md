# 控制子图周围和之间的间距

在这一步中，我们将使用 `GridSpec` 来控制子图周围和之间的间距。我们将创建一个包含 2 个网格布局（gridspec）的图形，每个网格布局有 3 行 3 列。我们将指定 `left`、`right`、`bottom`、`top`、`wspace` 和 `hspace` 参数来控制间距。

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
