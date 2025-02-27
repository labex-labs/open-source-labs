# Mehrklassen-Klassifikation

- Die `SVC`- und `NuSVC`-Klassifizierer können zur Mehrklassen-Klassifikation mit der "one-versus-one"-Methode verwendet werden:

```python
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)
dec = clf.decision_function([[1]])
```
