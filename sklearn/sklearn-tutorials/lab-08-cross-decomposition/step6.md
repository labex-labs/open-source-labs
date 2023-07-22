# PLSSVD

#### Fit the PLSSVD model

The `PLSSVD` algorithm is a simplified version of `PLSCanonical` that computes the Singular Value Decomposition (SVD) of the cross-covariance matrix only once. This algorithm is useful when the number of components is limited to one.

```python
plssvd = PLSSVD(n_components=1)
plssvd.fit(X, Y)
```

#### Transform the data

We can transform the original data using the fitted model. The transformed data will have reduced dimensions.

```python
X_transformed = plssvd.transform(X)
Y_transformed = plssvd.transform(Y)
```
