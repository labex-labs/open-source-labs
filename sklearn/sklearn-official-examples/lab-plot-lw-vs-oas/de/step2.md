# Daten generieren

Als nächstes werden wir Gaussian-verteilte Daten mit einer Kovarianzmatrix generieren, die einem AR(1)-Prozess folgt. Wir werden die Funktionen `toeplitz` und `cholesky` aus `scipy.linalg` verwenden, um die Kovarianzmatrix zu generieren.

```python
np.random.seed(0)

n_features = 100
r = 0.1
real_cov = toeplitz(r ** np.arange(n_features))
coloring_matrix = cholesky(real_cov)
```
