# 데이터 전처리

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

데이터셋을 학습용과 테스트용으로 분할하고, 입력 데이터를 `StandardScaler()` 함수를 사용하여 스케일링하여 데이터를 전처리합니다.
