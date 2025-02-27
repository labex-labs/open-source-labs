# MLPClassifier の訓練

40 個のニューロンを含む単一の隠れ層を持つ MLPClassifier を作成します。リソースの制約により、MLP を 8 回の反復だけ訓練します。また、制限された反復回数内でモデルが収束しないために投げられる `ConvergenceWarning` をキャッチします。

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
