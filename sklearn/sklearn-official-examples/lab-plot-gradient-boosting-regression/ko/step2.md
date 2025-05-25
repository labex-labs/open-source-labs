# 데이터 전처리

다음으로, 데이터셋을 훈련에 90% 를 사용하고 나머지를 테스트에 사용하도록 분할합니다. 또한 회귀 모델의 매개변수를 설정합니다.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=13)

params = {
    "n_estimators": 500,
    "max_depth": 4,
    "min_samples_split": 5,
    "learning_rate": 0.01,
    "loss": "squared_error",
}
```
