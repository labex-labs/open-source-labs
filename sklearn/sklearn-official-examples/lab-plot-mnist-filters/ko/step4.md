# 데이터 분할

`train_test_split` 함수를 사용하여 데이터셋을 학습용 데이터셋과 테스트용 데이터셋으로 분할합니다.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.7)
```
