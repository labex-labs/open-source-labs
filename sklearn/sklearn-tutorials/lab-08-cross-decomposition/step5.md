# CCA

#### Fit the CCA model

The `CCA` algorithm is a special case of PLS and stands for Canonical Correlation Analysis. It finds the correlation between two sets of variables.

```python
cca = CCA(n_components=2)
cca.fit(X, Y)
```

#### Transform the data

We can transform the original data using the fitted model. The transformed data will have reduced dimensions.

```python
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
```
