# Classificação Multi-classe

- Os classificadores `SVC` e `NuSVC` podem ser usados para classificação multi-classe utilizando a abordagem "um-contra-um":

```python
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)
dec = clf.decision_function([[1]])
```
