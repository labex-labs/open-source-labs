# Visualizar las proyecciones LLE y t-SNE del conjunto de datos Swiss-Hole

Podemos visualizar las proyecciones LLE y t-SNE del conjunto de datos Swiss-Hole utilizando diagramas de dispersión con diferentes colores que representan diferentes puntos.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sh_lle[:, 0], sh_lle[:, 1], c=sh_color)
axs[0].set_title("Proyección LLE de Swiss-Hole")
axs[1].scatter(sh_tsne[:, 0], sh_tsne[:, 1], c=sh_color)
_ = axs[1].set_title("Proyección t-SNE de Swiss-Hole")
```
