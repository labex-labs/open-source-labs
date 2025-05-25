# Definir Características Numéricas e Categóricas

Neste passo, definiremos as características numéricas e categóricas que utilizaremos no nosso pipeline. Também definiremos os pipelines de pré-processamento para dados numéricos e categóricos.

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
