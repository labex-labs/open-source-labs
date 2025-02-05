# 绘制测试集偏差

我们现在将为每种正则化策略绘制测试集偏差。

```python
plt.figure()

for label, color, setting in [
    ("无收缩", "橙色", {"learning_rate": 1.0, "subsample": 1.0}),
    ("learning_rate=0.2", "青绿色", {"learning_rate": 0.2, "subsample": 1.0}),
    ("subsample=0.5", "蓝色", {"learning_rate": 1.0, "subsample": 0.5}),
    (
        "learning_rate=0.2, subsample=0.5",
        "灰色",
        {"learning_rate": 0.2, "subsample": 0.5}
    ),
    (
        "learning_rate=0.2, max_features=2",
        "品红色",
        {"learning_rate": 0.2, "max_features": 2}
    )
]:
    params = dict(original_params)
    params.update(setting)

    clf = ensemble.GradientBoostingClassifier(**params)
    clf.fit(X_train, y_train)

    # 计算测试集偏差
    test_deviance = np.zeros((params["n_estimators"],), dtype=np.float64)

    for i, y_proba in enumerate(clf.staged_predict_proba(X_test)):
        test_deviance[i] = 2 * log_loss(y_test, y_proba[:, 1])

    plt.plot(
        (np.arange(test_deviance.shape[0]) + 1)[::5],
        test_deviance[::5],
        "-",
        color=color,
        label=label
    )

plt.legend(loc="upper right")
plt.xlabel("提升迭代次数")
plt.ylabel("测试集偏差")

plt.show()
```
