# Définir les fonctionnalités numériques et catégorielles

Dans cette étape, nous allons définir les fonctionnalités numériques et catégorielles que nous utiliserons pour notre pipeline. Nous allons également définir les pipelines de prétraitement pour les données numériques et catégorielles.

```python
numeric_features = ["age", "fare"]
numeric_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
)

categorical_features = ["embarked", "sex", "pclass"]
categorical_transformer = Pipeline(
    steps=[
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ("selector", SelectPercentile(chi2, percentile=50)),
    ]
)
```
