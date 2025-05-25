# Imputar Valores Ausentes com Simple Imputer

Usaremos a classe `SimpleImputer` do Scikit-Learn para imputar valores ausentes usando estratégias de média e mediana.

```python
score_simple_imputer = pd.DataFrame()
for strategy in ("mean", "median"):
    estimator = make_pipeline(
        SimpleImputer(missing_values=np.nan, strategy=strategy), BayesianRidge()
    )
    score_simple_imputer[strategy] = cross_val_score(
        estimator, X_missing, y_missing, scoring="neg_mean_squared_error", cv=N_SPLITS
    )
```
