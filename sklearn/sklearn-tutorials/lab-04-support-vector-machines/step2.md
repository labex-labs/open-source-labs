# Multi-class Classification

- The `SVC` and `NuSVC` classifiers can be used for multi-class classification using the "one-versus-one" approach:

```python
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)
dec = clf.decision_function([[1]])
```
