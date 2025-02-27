# Заполнение пропущенных значений с использованием SimpleImputer

Мы будем использовать класс `SimpleImputer` библиотеки Scikit-Learn для заполнения пропущенных значений с использованием стратегий среднего и медианы.

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
