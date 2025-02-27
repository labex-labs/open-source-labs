# Calculer les plongements LLE et t-SNE de l'ensemble de données Swiss-Hole

Nous calculons les plongements LLE et t-SNE de l'ensemble de données Swiss-Hole en utilisant les fonctions `manifold.locally_linear_embedding()` et `manifold.TSNE()` de `sklearn`, respectivement.

```python
sh_lle, sh_err = manifold.locally_linear_embedding(sh_points, n_neighbors=12, n_components=2)

sh_tsne = manifold.TSNE(n_components=2, perplexity=40, init="random", random_state=0).fit_transform(sh_points)
```
