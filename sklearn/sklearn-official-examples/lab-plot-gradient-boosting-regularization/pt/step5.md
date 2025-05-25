# Plotar Desvio do Conjunto de Teste

Agora, plotaremos o desvio do conjunto de teste para cada estratégia de regularização.

```python
plt.figure()

for label, color, setting in [
    ("Sem encolhimento", "orange", {"learning_rate": 1.0, "subsample": 1.0}),
    ("taxa_aprendizado=0.2", "turquoise", {"learning_rate": 0.2, "subsample": 1.0}),
    ("subsample=0.5", "blue", {"learning_rate": 1.0, "subsample": 0.5}),
    (
        "taxa_aprendizado=0.2, subsample=0.5",
        "gray",
        {"learning_rate": 0.2, "subsample": 0.5},
    ),
    (
        "taxa_aprendizado=0.2, max_features=2",
        "magenta",
        {"learning_rate": 0.2, "max_features": 2},
    ),
]:
    params = dict(original_params)
    params.update(setting)

    clf = ensemble.GradientBoostingClassifier(**params)
    clf.fit(X_train, y_train)

    # calcular o desvio do conjunto de teste
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
plt.xlabel("Iterações de Reforço")
plt.ylabel("Desvio do Conjunto de Teste")

plt.show()
```
