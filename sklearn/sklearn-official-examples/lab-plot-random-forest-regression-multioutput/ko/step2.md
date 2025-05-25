# 랜덤 데이터셋 생성

다음으로, 회귀에 사용할 랜덤 데이터셋을 생성합니다. `numpy`를 사용하여 -100 과 100 사이의 600 개의 x 값 집합과 x 값의 사인 및 코사인으로 계산된 y 값 (일부 랜덤 노이즈 포함) 을 생성합니다.

```python
rng = np.random.RandomState(1)
X = np.sort(200 * rng.rand(600, 1) - 100, axis=0)
y = np.array([np.pi * np.sin(X).ravel(), np.pi * np.cos(X).ravel()]).T
y += 0.5 - rng.rand(*y.shape)
```
