# 多クラス分類

- `SVC` と `NuSVC` 分類器は、「one-versus-one」アプローチを使って多クラス分類に使用できます：

```python
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)
dec = clf.decision_function([[1]])
```
