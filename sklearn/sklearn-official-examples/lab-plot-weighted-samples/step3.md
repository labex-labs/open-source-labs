# Create Sample Weights

We will create two sets of sample weights. The first set of sample weights will be constant for all points, and the second set of sample weights will be greater for some outliers.

```python
sample_weight_last_ten = abs(np.random.randn(len(X)))
sample_weight_constant = np.ones(len(X))
sample_weight_last_ten[15:] *= 5
sample_weight_last_ten[9] *= 15
```


