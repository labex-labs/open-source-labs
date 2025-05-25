# 데이터 생성

대상 값이 첫 번째 특징과 양의 상관관계를 가지고 두 번째 특징과 음의 상관관계를 갖는 인공 데이터 세트를 생성합니다. 또한 데이터를 더욱 현실적으로 만들기 위해 일부 랜덤 노이즈를 추가합니다.

```python
rng = np.random.RandomState(0)

n_samples = 1000
f_0 = rng.rand(n_samples)
f_1 = rng.rand(n_samples)
X = np.c_[f_0, f_1]
noise = rng.normal(loc=0.0, scale=0.01, size=n_samples)

y = 5 * f_0 + np.sin(10 * np.pi * f_0) - 5 * f_1 - np.cos(10 * np.pi * f_1) + noise
```
