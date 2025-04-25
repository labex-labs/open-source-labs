# スイスホールデータセットの LLE と t-SNE 埋め込みの可視化

異なる点を表す異なる色で散布図を使って、スイスホールデータセットの LLE と t-SNE 埋め込みを可視化することができます。

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sh_lle[:, 0], sh_lle[:, 1], c=sh_color)
axs[0].set_title("LLE Embedding of Swiss-Hole")
axs[1].scatter(sh_tsne[:, 0], sh_tsne[:, 1], c=sh_color)
_ = axs[1].set_title("t-SNE Embedding of Swiss-Hole")
```
