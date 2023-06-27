# Fit the Model

We will fit the model and get the separating hyperplane using the `SVC` function from the `svm` library. We will use a linear kernel and set `C` to 1.0.

```python
clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, y)
```
