# 단순 임퓨터를 이용한 누락 값 보간

Scikit-Learn 의 `SimpleImputer` 클래스를 사용하여 평균 및 중앙값 전략으로 누락된 값을 보간합니다.

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
