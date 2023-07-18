# Fit the isotonic regression model

Now, we can fit the isotonic regression model to our data. We create an instance of the `IsotonicRegression` class and call the `fit` method with our input data and target values.

```python
# Fit isotonic regression model
ir = IsotonicRegression()
ir.fit(X, y)
```
