# 可视化瑞士洞数据集的局部线性嵌入（LLE）和t-SNE嵌入

我们可以使用散点图来可视化瑞士洞数据集的局部线性嵌入（LLE）和t-SNE嵌入，其中不同颜色代表不同的点。

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sh_lle[:, 0], sh_lle[:, 1], c=sh_color)
axs[0].set_title("LLE Embedding of Swiss-Hole")
axs[1].scatter(sh_tsne[:, 0], sh_tsne[:, 1], c=sh_color)
_ = axs[1].set_title("t-SNE Embedding of Swiss-Hole")
```
