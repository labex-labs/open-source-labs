# 랜덤 분포 생성

로그정규, 카이제곱, 와이블, 가우시안, 균일, 이중봉 분포를 포함한 여섯 가지 서로 다른 확률 분포를 생성합니다.

```python
rng = np.random.RandomState(304)
bc = PowerTransformer(method="box-cox")
yj = PowerTransformer(method="yeo-johnson")
qt = QuantileTransformer(n_quantiles=500, output_distribution="normal", random_state=rng)
size = (N_SAMPLES, 1)

# 로그정규 분포
X_lognormal = rng.lognormal(size=size)

# 카이제곱 분포
df = 3
X_chisq = rng.chisquare(df=df, size=size)

# 와이블 분포
a = 50
X_weibull = rng.weibull(a=a, size=size)

# 가우시안 분포
loc = 100
X_gaussian = rng.normal(loc=loc, size=size)

# 균일 분포
X_uniform = rng.uniform(low=0, high=1, size=size)

# 이중봉 분포
loc_a, loc_b = 100, 105
X_a, X_b = rng.normal(loc=loc_a, size=size), rng.normal(loc=loc_b, size=size)
X_bimodal = np.concatenate([X_a, X_b], axis=0)
```
