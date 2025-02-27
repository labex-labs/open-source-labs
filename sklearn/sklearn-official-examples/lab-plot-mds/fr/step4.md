# Effectuer l'analyse en composantes principales multi-dimensionnelles (MDS)

Nous allons ensuite effectuer l'analyse en composantes principales multi-dimensionnelles sur l'ensemble de données bruité à l'aide de la classe MDS de scikit-learn. Nous utiliserons l'option de dissimilarité prédéfinie car nous avons déjà calculé les distances entre paires de points de données. Nous définirons également le nombre de composantes sur 2 pour une visualisation en 2D.

```python
mds = manifold.MDS(
    n_components=2,
    max_iter=3000,
    eps=1e-9,
    random_state=seed,
    dissimilarity="precomputed",
    n_jobs=1,
    normalized_stress="auto",
)
pos = mds.fit(similarities).embedding_
```
