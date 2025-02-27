# 近傍点グラフのキャッシュ

このステップでは、パイプラインのキャッシング機能を使って、KNeighborsClassifier の複数回のフィット間で近傍点グラフをキャッシュします。

```python
# 分類器のハイパーパラメータを調整する際に何度も使用されるグラフ計算をキャッシュするために、
# `memory` にグラフ計算をキャッシュするディレクトリを指定しています。
with TemporaryDirectory(prefix="sklearn_graph_cache_") as tmpdir:
    full_model = Pipeline(
        steps=[("graph", graph_model), ("classifier", classifier_model)], memory=tmpdir
    )
```
