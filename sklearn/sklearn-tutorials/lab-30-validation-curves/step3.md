# Plot the Validation Curve

Now, let's plot the validation curve using the `validation_curve` function. We will use the `Ridge` estimator and vary the `alpha` hyperparameter over a range of values.

```python
param_range = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(
    Ridge(), X, y, param_name="alpha", param_range=param_range, cv=5)
```
