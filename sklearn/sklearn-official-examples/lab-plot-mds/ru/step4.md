# Выполнение MDS

Затем мы выполним MDS на наборе данных с шумом с использованием класса MDS из scikit-learn. Мы будем использовать опцию предварительно вычисленных несовместимостей, так как мы уже вычислили попарные расстояния между точками данных. Также мы установим количество компонентов равным 2 для визуализации в 2D.

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
