# Visualize LLE and t-SNE Embeddings of Swiss Roll Dataset

We can visualize the LLE and t-SNE embeddings of the Swiss Roll dataset using scatter plots with different colors representing different points.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sr_lle[:, 0], sr_lle[:, 1], c=sr_color)
axs[0].set_title("LLE Embedding of Swiss Roll")
axs[1].scatter(sr_tsne[:, 0], sr_tsne[:, 1], c=sr_color)
_ = axs[1].set_title("t-SNE Embedding of Swiss Roll")
```
