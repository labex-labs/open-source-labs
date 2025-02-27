# Кешируем граф ближайших соседей

В этом шаге мы будем кешировать граф ближайших соседей между несколькими обучениями KNeighborsClassifier с использованием свойства кеширования в пайплайнах.

```python
# Note that we give `memory` a directory to cache the graph computation
# that will be used several times when tuning the hyperparameters of the
# classifier.
with TemporaryDirectory(prefix="sklearn_graph_cache_") as tmpdir:
    full_model = Pipeline(
        steps=[("graph", graph_model), ("classifier", classifier_model)], memory=tmpdir
    )
```
