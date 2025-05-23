# ランダムな分布の作成

6 つの異なる確率分布：対数正規分布、カイ二乗分布、ワイブル分布、ガウス分布、一様分布、および二峰性分布を生成します。

```python
rng = np.random.RandomState(304)
bc = PowerTransformer(method="box-cox")
yj = PowerTransformer(method="yeo-johnson")
qt = QuantileTransformer(n_quantiles=500, output_distribution="normal", random_state=rng)
size = (N_SAMPLES, 1)

# 対数正規分布
X_lognormal = rng.lognormal(size=size)

# カイ二乗分布
df = 3
X_chisq = rng.chisquare(df=df, size=size)

# ワイブル分布
a = 50
X_weibull = rng.weibull(a=a, size=size)

# ガウス分布
loc = 100
X_gaussian = rng.normal(loc=loc, size=size)

# 一様分布
X_uniform = rng.uniform(low=0, high=1, size=size)

# 二峰性分布
loc_a, loc_b = 100, 105
X_a, X_b = rng.normal(loc=loc_a, size=size), rng.normal(loc=loc_b, size=size)
X_bimodal = np.concatenate([X_a, X_b], axis=0)
```
