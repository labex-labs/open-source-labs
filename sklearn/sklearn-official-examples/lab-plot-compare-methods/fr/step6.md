# Embedding aléatoire voisin T-distribué

Il convertit les similitudes entre les points de données en probabilités conjointes et essaie de minimiser la divergence de Kullback-Leibler entre les probabilités conjointes de l'embedding à basse dimension et les données à haute dimension.

```python
t_sne = manifold.TSNE(
    n_components=n_components,
    perplexity=30,
    init="random",
    n_iter=250,
    random_state=0,
)
S_t_sne = t_sne.fit_transform(S_points)
```
