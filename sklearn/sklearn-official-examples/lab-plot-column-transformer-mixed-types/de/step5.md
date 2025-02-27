# Füge den Klassifizierer zur Vorverarbeitungspipeline hinzu

In diesem Schritt fügen wir den logistischen Regressionsklassifizierer zu unserer Vorverarbeitungspipeline hinzu, indem wir `Pipeline` verwenden.

```python
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
