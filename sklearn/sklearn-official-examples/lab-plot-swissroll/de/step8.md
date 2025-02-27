# Visualisierung von LLE- und t-SNE-Embeddings für den Swiss-Hole-Datensatz

Wir können die LLE- und t-SNE-Embeddings des Swiss-Hole-Datensatzes mithilfe von Streuplots visualisieren, wobei verschiedene Farben verschiedene Punkte repräsentieren.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sh_lle[:, 0], sh_lle[:, 1], c=sh_color)
axs[0].set_title("LLE Embedding of Swiss-Hole")
axs[1].scatter(sh_tsne[:, 0], sh_tsne[:, 1], c=sh_color)
_ = axs[1].set_title("t-SNE Embedding of Swiss-Hole")
```
