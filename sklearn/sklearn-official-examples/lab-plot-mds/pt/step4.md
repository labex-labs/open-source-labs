# Executar MDS

Em seguida, executaremos MDS no conjunto de dados ruidoso usando a classe MDS do scikit-learn. Usaremos a opção de dissimilaridade pré-calculada, pois já calculamos as distâncias de pares entre os pontos de dados. Também definiremos o número de componentes como 2 para visualização 2D.

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
