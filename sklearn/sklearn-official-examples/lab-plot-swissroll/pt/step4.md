# Visualizar as Embeddings LLE e t-SNE do Conjunto de Dados Swiss Roll

Podemos visualizar as embeddings LLE e t-SNE do conjunto de dados Swiss Roll usando gráficos de dispersão, com cores diferentes representando pontos diferentes.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sr_lle[:, 0], sr_lle[:, 1], c=sr_color)
axs[0].set_title("Embedding LLE do Swiss Roll")
axs[1].scatter(sr_tsne[:, 0], sr_tsne[:, 1], c=sr_color)
_ = axs[1].set_title("Embedding t-SNE do Swiss Roll")
```
