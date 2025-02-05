# 拟合估计器

第二步是将多输出估计器拟合到训练数据上。我们将使用四种不同的算法：极端随机树、k近邻、线性回归和岭回归。这些估计器将根据人脸的上半部分预测其下半部分。

```python
# 拟合估计器
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
