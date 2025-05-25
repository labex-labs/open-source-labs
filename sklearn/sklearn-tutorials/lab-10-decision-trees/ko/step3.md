# 데이터셋 분할

의사결정 트리 분류기를 학습하기 전에 데이터셋을 학습용과 테스트용으로 분할해야 합니다. 데이터의 70% 를 학습에, 30% 를 테스트에 사용할 것입니다.

```python
# 데이터셋을 학습용과 테스트용으로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```
