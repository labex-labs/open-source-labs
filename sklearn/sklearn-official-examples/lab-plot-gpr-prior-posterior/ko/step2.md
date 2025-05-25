# 학습 데이터 생성

다음으로, 여러 섹션에서 사용할 학습 데이터 세트를 생성합니다.

```python
rng = np.random.RandomState(4)
X_train = rng.uniform(0, 5, 10).reshape(-1, 1)
y_train = np.sin((X_train[:, 0] - 2.5) ** 2)
n_samples = 5
```
