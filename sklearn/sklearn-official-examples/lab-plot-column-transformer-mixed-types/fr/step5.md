# Ajouter le classifieur au pipeline de prétraitement

Dans cette étape, nous allons ajouter le classifieur de régression logistique à notre pipeline de prétraitement en utilisant `Pipeline`.

```python
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
