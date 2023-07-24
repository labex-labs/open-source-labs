# Fit a Gaussian Mixture Model

Now, we can fit a Gaussian Mixture Model to our data using the `GaussianMixture` class from the `sklearn.mixture` module. Specify the desired number of components and any other parameters you want to use.

```python
# Fit a Gaussian Mixture Model
gmm = GaussianMixture(n_components=3)
gmm.fit(X_train)
```
