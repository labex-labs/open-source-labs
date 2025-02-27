# Calculer les plongements LLE et t-SNE de l'ensemble de données Swiss Roll

Nous calculons les plongements LLE et t-SNE de l'ensemble de données Swiss Roll en utilisant les fonctions `manifold.locally_linear_embedding()` et `manifold.TSNE()` de `sklearn`, respectivement.

```python
sr_lle, sr_err = manifold.locally_linear_embedding(sr_points, n_neighbors=12, n_components=2)

sr_tsne = manifold.TSNE(n_components=2, perplexity=40, random_state=0).fit_transform(sr_points)
```
