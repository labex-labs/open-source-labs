# 다중 클래스 분류

- `SVC` 및 `NuSVC` 분류기는 "일대일" 접근 방식을 사용하여 다중 클래스 분류에 사용할 수 있습니다.

```python
X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
clf = svm.SVC(decision_function_shape='ovo')
clf.fit(X, Y)
dec = clf.decision_function([[1]])
```
