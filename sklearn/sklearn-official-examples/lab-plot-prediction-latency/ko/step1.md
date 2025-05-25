# 회귀 데이터셋 생성

Scikit-Learn 의 `make_regression` 함수를 사용하여 주어진 매개변수로 회귀 데이터셋을 생성합니다. 데이터셋은 `n_train`개의 학습 인스턴스, `n_test`개의 테스트 인스턴스, `n_features`개의 특징, 그리고 0.1 의 `noise`를 가집니다.

```python
X, y, coef = make_regression(
    n_samples=n_train + n_test, n_features=n_features, noise=noise, coef=True
)

random_seed = 13
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_train, test_size=n_test, random_state=random_seed
)
X_train, y_train = shuffle(X_train, y_train, random_state=random_seed)

X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

y_scaler = StandardScaler()
y_train = y_scaler.fit_transform(y_train[:, None])[:, 0]
y_test = y_scaler.transform(y_test[:, None])[:, 0]
```
