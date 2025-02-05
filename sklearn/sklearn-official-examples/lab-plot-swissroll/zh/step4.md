# 可视化瑞士卷数据集的局部线性嵌入（LLE）和t-SNE嵌入

我们可以使用散点图来可视化瑞士卷数据集的局部线性嵌入（LLE）和t-SNE嵌入，不同颜色代表不同的点。

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sr_lle[:, 0], sr_lle[:, 1], c=sr_color)
axs[0].set_title("LLE Embedding of Swiss Roll")
axs[1].scatter(sr_tsne[:, 0], sr_tsne[:, 1], c=sr_color)
_ = axs[1].set_title("t-SNE Embedding of Swiss Roll")
```
