# Visualisierung von LLE- und t-SNE-Embeddings für den Swiss Roll-Datensatz

Wir können die LLE- und t-SNE-Embeddings des Swiss Roll-Datensatzes mithilfe von Streuplots visualisieren, wobei verschiedene Farben verschiedene Punkte repräsentieren.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sr_lle[:, 0], sr_lle[:, 1], c=sr_color)
axs[0].set_title("LLE Embedding of Swiss Roll")
axs[1].scatter(sr_tsne[:, 0], sr_tsne[:, 1], c=sr_color)
_ = axs[1].set_title("t-SNE Embedding of Swiss Roll")
```
