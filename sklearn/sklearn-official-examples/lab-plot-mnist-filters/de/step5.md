# MLPClassifier trainieren

Wir erstellen einen MLPClassifier (Multi-Layer Perceptron Classifier) mit einer einzigen versteckten Schicht, die 40 Neuronen enthält. Aufgrund von Ressourcenbeschränkungen trainieren wir das MLP nur für 8 Iterationen. Wir fangen auch die `ConvergenceWarning` (Konvergenzwarnung) ab, die geworfen wird, weil das Modell innerhalb der begrenzten Anzahl von Iterationen nicht konvergieren wird.

```python
mlp = MLPClassifier(
    hidden_layer_sizes=(40,),
    max_iter=8,
    alpha=1e-4,
    solver="sgd",
    verbose=10,
    random_state=1,
    learning_rate_init=0.2,
)

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")
    mlp.fit(X_train, y_train)
```
