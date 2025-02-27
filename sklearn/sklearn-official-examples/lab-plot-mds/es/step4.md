# Realizar MDS

Luego, realizaremos MDS en el conjunto de datos ruidoso utilizando la clase MDS de scikit-learn. Utilizaremos la opción de disimilitud precomputada ya que ya hemos calculado las distancias entre pares de puntos de datos. También estableceremos el número de componentes en 2 para la visualización en 2D.

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
