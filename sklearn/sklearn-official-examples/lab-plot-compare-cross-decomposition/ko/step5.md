# CCA (대칭적 팽창을 갖는 PLS 모드 B)

데이터를 변환하기 위해 CCA 알고리즘을 사용합니다.

```python
cca = CCA(n_components=2)
cca.fit(X_train, Y_train)
X_train_r, Y_train_r = cca.transform(X_train, Y_train)
X_test_r, Y_test_r = cca.transform(X_test, Y_test)
```
