# Utiliser l'algorithme FastICA

Dans cette étape, nous utilisons l'algorithme FastICA, qui trouve des directions dans l'espace de caractéristiques correspondant à des projections avec une forte non-gaussianité.

```python
ica = FastICA(random_state=rng, whiten="arbitrary-variance")
S_ica_ = ica.fit(X).transform(X)  # Estimate the sources

S_ica_ /= S_ica_.std(axis=0)
```
