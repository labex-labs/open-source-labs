# Création de distributions aléatoires

Nous allons générer six distributions de probabilité différentes : Lognormale, Khi-carré, Weibull, Gaussienne, Uniforme et Bimodale.

```python
rng = np.random.RandomState(304)
bc = PowerTransformer(method="box-cox")
yj = PowerTransformer(method="yeo-johnson")
qt = QuantileTransformer(n_quantiles=500, output_distribution="normal", random_state=rng)
size = (N_SAMPLES, 1)

# distribution lognormale
X_lognormal = rng.lognormal(size=size)

# distribution khi-carré
df = 3
X_chisq = rng.chisquare(df=df, size=size)

# distribution weibull
a = 50
X_weibull = rng.weibull(a=a, size=size)

# distribution gaussienne
loc = 100
X_gaussian = rng.normal(loc=loc, size=size)

# distribution uniforme
X_uniform = rng.uniform(low=0, high=1, size=size)

# distribution bimodale
loc_a, loc_b = 100, 105
X_a, X_b = rng.normal(loc=loc_a, size=size), rng.normal(loc=loc_b, size=size)
X_bimodal = np.concatenate([X_a, X_b], axis=0)
```
