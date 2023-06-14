# Train MLPClassifier

We will create an MLPClassifier with a single hidden layer containing 40 neurons. We will train the MLP for only 8 iterations due to resource constraints. We will also catch the `ConvergenceWarning` that will be thrown because the model won't converge within the limited number of iterations.

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


