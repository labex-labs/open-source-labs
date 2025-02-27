# Независимые компоненты - FastICA

Метод анализа независимых компонент (Independent Component Analysis - ICA) - это метод разделения многомерных сигналов на аддитивные подкомпоненты, которые максимально независимы. Мы применяем FastICA, который представляет собой быстрый и надежный алгоритм для ICA.

```python
# Independent components - FastICA
ica_estimator = decomposition.FastICA(
    n_components=n_components, max_iter=400, whiten="arbitrary-variance", tol=15e-5
)
ica_estimator.fit(faces_centered)
plot_gallery(
    "Independent components - FastICA", ica_estimator.components_[:n_components]
)
```
