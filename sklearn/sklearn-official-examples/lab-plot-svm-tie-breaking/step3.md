# Create SVM Model with and without Tie-Breaking

In this step, we will create two SVM models - one with tie-breaking disabled and another with tie-breaking enabled. We will use the `SVC` class from scikit-learn to create these models. The `break_ties` parameter is set to `False` and `True` for the two models, respectively.

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```


