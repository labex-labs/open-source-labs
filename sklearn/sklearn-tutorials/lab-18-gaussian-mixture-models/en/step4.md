# Cluster the data

Once the model has been fit, we can use it to cluster the data by assigning each sample to the Gaussian component it belongs to. The `predict` method of the `GaussianMixture` class can be used for this purpose.

```python
# Cluster the data
cluster_labels = gmm.predict(X_test)
```
