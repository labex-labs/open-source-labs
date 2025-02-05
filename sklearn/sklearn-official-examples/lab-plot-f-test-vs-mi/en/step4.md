# Calculate mutual information

We will now calculate the mutual information score for each feature. Mutual information can capture any kind of dependency between variables. We will normalize the mutual information scores by dividing them by the maximum mutual information score.

```python
mi = mutual_info_regression(X, y)
mi /= np.max(mi)
```
