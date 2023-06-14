# Fit the Model with Weighted Classes

We will fit the model and get the separating hyperplane using the `SVC` function from the `svm` library. We will use a linear kernel and set `class_weight` to `{1: 10}`. This will give more weight to the smaller class.

```python
wclf = svm.SVC(kernel="linear", class_weight={1: 10})
wclf.fit(X, y)
```


