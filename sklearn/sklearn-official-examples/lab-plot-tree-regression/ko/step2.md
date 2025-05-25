# 랜덤 데이터셋 생성

NumPy 를 사용하여 랜덤 데이터셋을 생성하고 일부 잡음을 추가합니다.

```python
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
```
