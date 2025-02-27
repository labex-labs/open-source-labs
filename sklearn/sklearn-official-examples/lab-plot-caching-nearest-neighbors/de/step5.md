# Caching des Nachbargraphen

In diesem Schritt werden wir den Nachbargraphen zwischen mehreren Anpassungen von KNeighborsClassifier mithilfe der Caching-Eigenschaft von Pipelines cachen.

```python
# Beachten Sie, dass wir `memory` ein Verzeichnis geben, um die Graphberechnung zu cachen,
# die mehrmals verwendet wird, wenn die Hyperparameter des Klassifiziers optimiert werden.
with TemporaryDirectory(prefix="sklearn_graph_cache_") as tmpdir:
    full_model = Pipeline(
        steps=[("graph", graph_model), ("classifier", classifier_model)], memory=tmpdir
    )
```
