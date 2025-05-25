# 전처리

데이터를 섞고, 학습 및 테스트 데이터셋으로 분할하고, `StandardScaler`를 사용하여 데이터를 스케일링하여 데이터를 전처리합니다.

```python
random_state = check_random_state(0)
permutation = random_state.permutation(X.shape[0])
X = X[permutation]
y = y[permutation]
X = X.reshape((X.shape[0], -1))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=train_samples, test_size=10000
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
