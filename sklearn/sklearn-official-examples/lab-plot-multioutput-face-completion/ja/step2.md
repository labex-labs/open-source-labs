# 推定器の適合

2番目のステップは、訓練データに対して多出力推定器を適合させることです。4つの異なるアルゴリズムを使用します。極端にランダム化された木、k近傍法、線形回帰、およびリッジ回帰。推定器は、上半分に基づいて顔の下半分を予測します。

```python
# Fit estimators
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(
        n_estimators=10, max_features=32, random_state=0
    ),
    "K-nn": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)
```
