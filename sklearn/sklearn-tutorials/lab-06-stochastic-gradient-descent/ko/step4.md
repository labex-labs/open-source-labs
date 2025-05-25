# 데이터 분할

데이터셋을 학습용 데이터셋과 테스트용 데이터셋으로 분할합니다. 학습용 데이터셋은 SGD 분류기를 학습하는 데 사용되고, 테스트용 데이터셋은 분류기의 성능을 평가하는 데 사용됩니다.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
