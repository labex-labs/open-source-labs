# Fit Isotonic and Linear Regression Models

We will now fit both the isotonic and linear regression models to the generated data.

```python
ir = IsotonicRegression(out_of_bounds="clip")
y_ = ir.fit_transform(x, y)

lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x needs to be 2d for LinearRegression
```


