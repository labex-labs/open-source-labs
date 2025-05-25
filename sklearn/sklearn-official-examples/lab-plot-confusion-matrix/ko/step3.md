# 데이터 분할

데이터셋을 학습용 데이터셋과 테스트용 데이터셋으로 분할할 것입니다. 학습용 데이터셋은 모델을 학습하는 데 사용되고, 테스트용 데이터셋은 모델의 성능을 평가하는 데 사용됩니다.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
