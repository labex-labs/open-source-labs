# Clasificación multi-clase

- Los clasificadores `SVC` y `NuSVC` se pueden utilizar para la clasificación multi-clase utilizando el enfoque "uno contra uno":

```python
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)
dec = clf.decision_function([[1]])
```
