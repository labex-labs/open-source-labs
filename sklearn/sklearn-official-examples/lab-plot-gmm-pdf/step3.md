# Fit Gaussian Mixture Model

We will now fit a GMM to the dataset using the GaussianMixture class from scikit-learn. We will set the number of components to 2 and the covariance type to "full".

```python
# fit a Gaussian Mixture Model with two components
clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)
```
