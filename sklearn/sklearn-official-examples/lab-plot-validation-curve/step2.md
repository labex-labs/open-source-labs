# Defining the Hyperparameter Range

We will define a range of values for the SVM kernel parameter gamma that we want to test.

```python
param_range = np.logspace(-6, -1, 5)
```
