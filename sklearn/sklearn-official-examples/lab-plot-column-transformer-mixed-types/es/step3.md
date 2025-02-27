# Definir características numéricas y categóricas

En este paso, definiremos las características numéricas y categóricas que utilizaremos para nuestro flujo de trabajo. También definiremos los flujos de preprocesamiento para los datos numéricos y categóricos.

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
