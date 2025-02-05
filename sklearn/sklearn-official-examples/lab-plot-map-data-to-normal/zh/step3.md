# 创建随机分布

我们将生成六种不同的概率分布：对数正态分布、卡方分布、威布尔分布、高斯分布、均匀分布和双峰分布。

```python
rng = np.random.RandomState(304)
bc = PowerTransformer(method="box-cox")
yj = PowerTransformer(method="yeo-johnson")
qt = QuantileTransformer(n_quantiles=500, output_distribution="normal", random_state=rng)
size = (N_SAMPLES, 1)

# 对数正态分布
X_lognormal = rng.lognormal(size=size)

# 卡方分布
df = 3
X_chisq = rng.chisquare(df=df, size=size)

# 威布尔分布
a = 50
X_weibull = rng.weibull(a=a, size=size)

# 高斯分布
loc = 100
X_gaussian = rng.normal(loc=loc, size=size)

# 均匀分布
X_uniform = rng.uniform(low=0, high=1, size=size)

# 双峰分布
loc_a, loc_b = 100, 105
X_a, X_b = rng.normal(loc=loc_a, size=size), rng.normal(loc=loc_b, size=size)
X_bimodal = np.concatenate([X_a, X_b], axis=0)
```
