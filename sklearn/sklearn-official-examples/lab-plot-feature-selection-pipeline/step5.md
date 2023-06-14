# Inspect the Pipeline

We can inspect the pipeline to better understand the model. We can use the index of the selected features to retrieve the original feature names.

```python
anova_svm[:-1].inverse_transform(anova_svm[-1].coef_)
```
