# Imputation des valeurs manquantes avec SimpleImputer

Nous allons utiliser la classe `SimpleImputer` de Scikit-Learn pour imputer les valeurs manquantes en utilisant les stratégies de moyenne et de médiane.

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
