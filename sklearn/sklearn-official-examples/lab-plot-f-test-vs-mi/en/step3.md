# Calculate F-test

We will now calculate the F-test score for each feature. F-test captures only linear dependency between variables. We will normalize the F-test scores by dividing them by the maximum F-test score.

```python
f_test, _ = f_regression(X, y)
f_test /= np.max(f_test)
```
