# Create Classifiers

We will create MLP classifiers for each value of alpha. We will create a pipeline that includes StandardScaler to standardize the data and MLPClassifier with different values of alpha. We will set the solver to 'lbfgs', which is an optimizer in the family of quasi-Newton methods. We will set max_iter to 2000 and early_stopping to True to prevent overfitting. We will use two hidden layers with 10 neurons each.

```python
classifiers = []
names = []
for alpha in alphas:
    classifiers.append(
        make_pipeline(
            StandardScaler(),
            MLPClassifier(
                solver="lbfgs",
                alpha=alpha,
                random_state=1,
                max_iter=2000,
                early_stopping=True,
                hidden_layer_sizes=[10, 10],
            ),
        )
    )
    names.append(f"alpha {alpha:.2f}")
```
