# MLPClassifier trainieren

Wir werden einen MLPClassifier mit einer einzigen versteckten Schicht erstellen, die 40 Neuronen enthält. Aufgrund von Ressourcenbeschränkungen werden wir das MLP nur für 8 Iterationen trainieren. Wir werden auch die `ConvergenceWarning` fangen, die ausgelöst wird, weil das Modell innerhalb der begrenzten Anzahl an Iterationen nicht konvergieren wird.

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