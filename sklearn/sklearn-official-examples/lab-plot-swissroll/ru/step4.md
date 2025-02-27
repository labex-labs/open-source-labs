# Визуализация эмбеддингов LLE и t-SNE для набора данных Swiss Roll

Можем визуализировать эмбеддинги LLE и t-SNE для набора данных Swiss Roll с использованием точечных диаграмм, где разные цвета представляют разные точки.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sr_lle[:, 0], sr_lle[:, 1], c=sr_color)
axs[0].set_title("Эмбеддинг LLE для Swiss Roll")
axs[1].scatter(sr_tsne[:, 0], sr_tsne[:, 1], c=sr_color)
_ = axs[1].set_title("Эмбеддинг t-SNE для Swiss Roll")
```
