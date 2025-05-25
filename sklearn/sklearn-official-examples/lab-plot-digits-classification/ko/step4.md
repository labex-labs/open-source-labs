# 데이터셋 분할

`sklearn.model_selection`의 `train_test_split()` 메서드를 사용하여 데이터셋을 50% 훈련 및 50% 테스트 하위 집합으로 분할합니다.

```python
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
```
