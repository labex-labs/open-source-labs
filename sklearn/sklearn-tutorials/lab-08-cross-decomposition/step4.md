# PLSCanonical

#### Fit the PLSCanonical model

Next, we'll use the `PLSCanonical` algorithm, which finds the canonical correlation between two matrices. This algorithm is useful when there is multicollinearity among the features.

```python
plsc = PLSCanonical(n_components=2)
plsc.fit(X, Y)
```

#### Transform the data

We can transform the original data using the fitted model. The transformed data will have reduced dimensions.

```python
X_transformed = plsc.transform(X)
Y_transformed = plsc.transform(Y)
```
