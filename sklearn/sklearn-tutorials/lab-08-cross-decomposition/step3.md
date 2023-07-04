# PLSRegression

#### Fit the PLSRegression model

We'll start with the `PLSRegression` algorithm, which is a form of regularized linear regression. We'll fit the model to our data.

```python
pls = PLSRegression(n_components=2)
pls.fit(X, Y)
```

#### Transform the data

We can transform the original data using the fitted model. The transformed data will have reduced dimensions.

```python
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)
```
