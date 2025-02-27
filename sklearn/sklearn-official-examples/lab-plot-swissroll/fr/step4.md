# Visualiser les plongements LLE et t-SNE de l'ensemble de données Swiss Roll

Nous pouvons visualiser les plongements LLE et t-SNE de l'ensemble de données Swiss Roll en utilisant des nuages de points avec des couleurs différentes représentant différents points.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sr_lle[:, 0], sr_lle[:, 1], c=sr_color)
axs[0].set_title("Plongement LLE de Swiss Roll")
axs[1].scatter(sr_tsne[:, 0], sr_tsne[:, 1], c=sr_color)
_ = axs[1].set_title("Plongement t-SNE de Swiss Roll")
```
