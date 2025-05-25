# SVM 을 이용한 회귀

- 회귀 문제의 경우, SVM 은 `SVR` 클래스를 사용하여 수행할 수 있습니다.

```python
X = [[0, 0], [1, 1]]
y = [0.5, 2.5]
regr = svm.SVR()
regr.fit(X, y)
regr.predict([[1, 1]])
```
