# Generate New Samples

We use the best estimator to sample 44 new points from the data. We then transform the new data back to its original 64 dimension using the inverse of PCA.

```python
# sample 44 new points from the data
new_data = kde.sample(44, random_state=0)
new_data = pca.inverse_transform(new_data)
```


