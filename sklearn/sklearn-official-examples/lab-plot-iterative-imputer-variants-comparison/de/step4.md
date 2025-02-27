# Fehlende Werte mit SimpleImputer ergänzen

Wir werden die `SimpleImputer`-Klasse von Scikit-Learn verwenden, um fehlende Werte mit Mittelwert- und Medianstrategien zu ergänzen.

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
