# 테스트 세트 편차 플롯

이제 각 정규화 전략에 대한 테스트 세트 편차를 플롯합니다.

```python
plt.figure()

for label, color, setting in [
    ("축소 없음", "orange", {"learning_rate": 1.0, "subsample": 1.0}),
    ("학습률=0.2", "turquoise", {"learning_rate": 0.2, "subsample": 1.0}),
    ("샘플링 비율=0.5", "blue", {"learning_rate": 1.0, "subsample": 0.5}),
    (
        "학습률=0.2, 샘플링 비율=0.5",
        "gray",
        {"learning_rate": 0.2, "subsample": 0.5},
    ),
    (
        "학습률=0.2, 최대 특징=2",
        "magenta",
        {"learning_rate": 0.2, "max_features": 2},
    ),
]:
    params = dict(original_params)
    params.update(setting)

    clf = ensemble.GradientBoostingClassifier(**params)
    clf.fit(X_train, y_train)

    # 테스트 세트 편차 계산
    test_deviance = np.zeros((params["n_estimators"],), dtype=np.float64)

    for i, y_proba in enumerate(clf.staged_predict_proba(X_test)):
        test_deviance[i] = 2 * log_loss(y_test, y_proba[:, 1])

    plt.plot(
        (np.arange(test_deviance.shape[0]) + 1)[::5],
        test_deviance[::5],
        "-",
        color=color,
        label=label,
    )

plt.legend(loc="upper right")
plt.xlabel("부스팅 반복 횟수")
plt.ylabel("테스트 세트 편차")

plt.show()
```
