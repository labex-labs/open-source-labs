# Визуализация эмбеддингов LLE и t-SNE для набора данных Swiss-Hole

Можем визуализировать эмбеддинги LLE и t-SNE для набора данных Swiss-Hole с использованием точечных диаграмм, где разные цвета представляют разные точки.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sh_lle[:, 0], sh_lle[:, 1], c=sh_color)
axs[0].set_title("Эмбеддинг LLE для Swiss-Hole")
axs[1].scatter(sh_tsne[:, 0], sh_tsne[:, 1], c=sh_color)
_ = axs[1].set_title("Эмбеддинг t-SNE для Swiss-Hole")
```
