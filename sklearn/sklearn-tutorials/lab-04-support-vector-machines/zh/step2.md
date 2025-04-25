# 多类分类

- `SVC` 和 `NuSVC` 分类器可使用“一对多”方法用于多类分类：

```python
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)
dec = clf.decision_function([[1]])
```
