# Построим откланение на тестовом наборе

Теперь построим откланение на тестовом наборе для каждой стратегии регуляризации.

```python
plt.figure()

for label, color, setting in [
    ("Без уменьшения (shrinkage)", "оранжевый", {"learning_rate": 1.0, "subsample": 1.0}),
    ("learning_rate=0.2", "бирюзовый", {"learning_rate": 0.2, "subsample": 1.0}),
    ("subsample=0.5", "синий", {"learning_rate": 1.0, "subsample": 0.5}),
    (
        "learning_rate=0.2, subsample=0.5",
        "серый",
        {"learning_rate": 0.2, "subsample": 0.5},
    ),
    (
        "learning_rate=0.2, max_features=2",
        "магента",
        {"learning_rate": 0.2, "max_features": 2},
    ),
]:
    params = dict(original_params)
    params.update(setting)

    clf = ensemble.GradientBoostingClassifier(**params)
    clf.fit(X_train, y_train)

    # вычислим откланение на тестовом наборе
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
plt.xlabel("Итерации бустинга")
plt.ylabel("Откланение на тестовом наборе")

plt.show()
```
