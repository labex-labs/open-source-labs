# Executar MDS Não-Métrico

Também executaremos MDS não-métrico no mesmo conjunto de dados para comparação. Usaremos as mesmas opções que o MDS, exceto que definiremos a opção métrica como False.

```python
nmds = manifold.MDS(
    n_components=2,
    metric=False,
    max_iter=3000,
    eps=1e-12,
    dissimilarity="precomputed",
    random_state=seed,
    n_jobs=1,
    n_init=1,
    normalized_stress="auto",
)
npos = nmds.fit_transform(similarities, init=pos)
```
