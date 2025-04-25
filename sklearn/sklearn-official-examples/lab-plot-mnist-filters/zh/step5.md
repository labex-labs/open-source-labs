# 训练多层感知器分类器（MLPClassifier）

我们将创建一个具有单个隐藏层且包含 40 个神经元的多层感知器分类器。由于资源限制，我们将仅训练该多层感知器 8 次迭代。我们还将捕获由于模型在有限的迭代次数内无法收敛而抛出的 `ConvergenceWarning`（收敛警告）。

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
