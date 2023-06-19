# Evaluate the Coefficients of the Linear Model with Cross Validation

The coefficients of the linear model show that most of the weight is on the feature at column index 0, which is the informative feature. Run the following code to evaluate the coefficients of the linear model with cross-validation:

```python
coefs_cv = pd.Series(
    model_with_cv[-1].coef_, index=model_with_cv[-1].feature_names_in_
).sort_values()
_ = coefs_cv.plot(kind="barh")
```


