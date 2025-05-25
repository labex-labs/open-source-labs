# 데이터 분할

이 단계에서는 `train_test_split` 함수를 사용하여 데이터를 학습용 및 테스트용 집합으로 분할합니다.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```
