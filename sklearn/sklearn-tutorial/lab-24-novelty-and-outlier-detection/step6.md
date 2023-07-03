# Access outlier scores

In addition to predicting outliers, we can also access the outlier scores for each observation using the `negative_outlier_factor_` attribute. Lower outlier scores indicate higher abnormality.

```python
outlier_scores = estimator.negative_outlier_factor_
print(outlier_scores)
```

#
