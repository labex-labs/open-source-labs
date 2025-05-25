# Visualizar os Embeddings LLE e t-SNE do Conjunto de Dados Swiss-Hole

Podemos visualizar os embeddings LLE e t-SNE do conjunto de dados Swiss-Hole usando gráficos de dispersão, com cores diferentes representando pontos diferentes.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sh_lle[:, 0], sh_lle[:, 1], c=sh_color)
axs[0].set_title("Embedding LLE do Swiss-Hole")
axs[1].scatter(sh_tsne[:, 0], sh_tsne[:, 1], c=sh_color)
_ = axs[1].set_title("Embedding t-SNE do Swiss-Hole")
```
