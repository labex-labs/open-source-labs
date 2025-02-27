# Pipeline de prise en charge native des variables catégorielles

Nous allons créer un pipeline dans lequel nous utilisons la prise en charge native des variables catégorielles de l'estimateur HistGradientBoostingRegressor pour traiter les variables catégorielles. Nous allons toujours utiliser un OrdinalEncoder pour prétraiter les données.

```python
hist_native = make_pipeline(
    ordinal_encoder,
    HistGradientBoostingRegressor(
        random_state=42,
        categorical_features=categorical_columns,
    ),
).set_output(transform="pandas")
```
