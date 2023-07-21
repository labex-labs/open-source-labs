# Evaluate the Coefficients of the Linear Model without Cross Validation

The Ridge model overfits because it assigns more weight to the extremely high cardinality feature relative to the informative feature. Run the following code to evaluate the coefficients of the linear model without cross-validation:

```python
coefs_no_cv = pd.Series(
    model_no_cv.coef_, index=model_no_cv.feature_names_in_
).sort_values()
_ = coefs_no_cv.plot(kind="barh")
```
