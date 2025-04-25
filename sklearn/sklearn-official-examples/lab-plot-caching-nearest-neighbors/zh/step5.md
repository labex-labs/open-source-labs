# 缓存最近邻图

在这一步中，我们将利用管道的缓存属性，在 KNeighborsClassifier 的多次拟合之间缓存最近邻图。

```python
# 请注意，我们给 `memory` 一个目录来缓存图计算，在调整分类器的超参数时，这个计算会被多次使用。
with TemporaryDirectory(prefix="sklearn_graph_cache_") as tmpdir:
    full_model = Pipeline(
        steps=[("graph", graph_model), ("classifier", classifier_model)], memory=tmpdir
    )
```
