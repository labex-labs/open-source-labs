# Append the Classifier to Preprocessing Pipeline

In this step, we will append the logistic regression classifier to our preprocessing pipeline using `Pipeline`.

```python
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
