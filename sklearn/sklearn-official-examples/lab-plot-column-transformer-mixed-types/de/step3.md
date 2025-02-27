# Definiere numerische und kategorische Merkmale

In diesem Schritt definieren wir die numerischen und kategorischen Merkmale, die wir für unsere Pipeline verwenden werden. Wir definieren auch die Aufbereitungspipelines für sowohl numerische als auch kategorische Daten.

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
