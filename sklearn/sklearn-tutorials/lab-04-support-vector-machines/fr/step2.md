# Classification multi-classe

- Les classifieurs `SVC` et `NuSVC` peuvent être utilisés pour la classification multi-classe en utilisant l'approche "un-versus-un" :

```python
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)
dec = clf.decision_function([[1]])
```
