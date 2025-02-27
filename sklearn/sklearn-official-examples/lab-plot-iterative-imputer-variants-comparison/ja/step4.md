# SimpleImputerを使った欠損値の補完

Scikit-Learnの`SimpleImputer`クラスを使って、平均値と中央値の戦略を用いて欠損値を補完します。

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
