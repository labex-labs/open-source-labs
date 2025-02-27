# Visualizar las proyecciones LLE y t-SNE del conjunto de datos Swiss Roll

Podemos visualizar las proyecciones LLE y t-SNE del conjunto de datos Swiss Roll utilizando diagramas de dispersión con diferentes colores que representan diferentes puntos.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sr_lle[:, 0], sr_lle[:, 1], c=sr_color)
axs[0].set_title("Proyección LLE de Swiss Roll")
axs[1].scatter(sr_tsne[:, 0], sr_tsne[:, 1], c=sr_color)
_ = axs[1].set_title("Proyección t-SNE de Swiss Roll")
```
