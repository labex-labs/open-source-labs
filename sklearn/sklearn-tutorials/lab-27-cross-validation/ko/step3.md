# 데이터셋을 학습 및 테스트 데이터로 분할

모델의 성능을 평가하기 위해 데이터셋을 학습 데이터와 테스트 데이터로 분할해야 합니다. `train_test_split` 함수를 사용하여 이 작업을 수행합니다.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
```
