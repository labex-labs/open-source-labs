# Criar Distribuições Aleatórias

Vamos gerar seis distribuições de probabilidade diferentes: Lognormal, Qui-quadrado, Weibull, Gaussiana, Uniforme e Bimodal.

```python
rng = np.random.RandomState(304)
bc = PowerTransformer(method="box-cox")
yj = PowerTransformer(method="yeo-johnson")
qt = QuantileTransformer(n_quantiles=500, output_distribution="normal", random_state=rng)
size = (N_SAMPLES, 1)

# distribuição lognormal
X_lognormal = rng.lognormal(size=size)

# distribuição qui-quadrado
df = 3
X_chisq = rng.chisquare(df=df, size=size)

# distribuição weibull
a = 50
X_weibull = rng.weibull(a=a, size=size)

# distribuição gaussiana
loc = 100
X_gaussian = rng.normal(loc=loc, size=size)

# distribuição uniforme
X_uniform = rng.uniform(low=0, high=1, size=size)

# distribuição bimodal
loc_a, loc_b = 100, 105
X_a, X_b = rng.normal(loc=loc_a, size=size), rng.normal(loc=loc_b, size=size)
X_bimodal = np.concatenate([X_a, X_b], axis=0)
```
