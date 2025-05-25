# 데이터셋 분할

데이터셋을 학습용과 테스트용으로 분할합니다. 처음 3000 개의 샘플을 학습용으로, 나머지 샘플을 테스트용으로 사용합니다.

```python
n_split = 3000
X_train, X_test = X[:n_split], X[n_split:]
y_train, y_test = y[:n_split], y[n_split:]
```
