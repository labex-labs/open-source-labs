# Visualiser les plongements LLE et t-SNE de l'ensemble de données Swiss-Hole

Nous pouvons visualiser les plongements LLE et t-SNE de l'ensemble de données Swiss-Hole en utilisant des nuages de points avec des couleurs différentes représentant différents points.

```python
fig, axs = plt.subplots(figsize=(8, 8), nrows=2)
axs[0].scatter(sh_lle[:, 0], sh_lle[:, 1], c=sh_color)
axs[0].set_title("Plongement LLE de Swiss-Hole")
axs[1].scatter(sh_tsne[:, 0], sh_tsne[:, 1], c=sh_color)
_ = axs[1].set_title("Plongement t-SNE de Swiss-Hole")
```
