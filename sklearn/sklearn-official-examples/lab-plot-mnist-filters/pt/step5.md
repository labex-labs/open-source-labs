# Treinar MLPClassifier

Criaremos um classificador MLPClassifier com uma única camada oculta contendo 40 neurônios. Treinaremos o MLP por apenas 8 iterações devido a restrições de recursos. Também capturaremos o `ConvergenceWarning` que será lançado porque o modelo não convergirá dentro do número limitado de iterações.

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
