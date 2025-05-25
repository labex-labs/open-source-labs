# Gerar um conjunto de dados de brinquedo

O próximo passo é gerar um conjunto de dados de brinquedo, que é uma linha reta com algum ruído gaussiano. Usaremos `numpy` para gerar este conjunto de dados.

```python
# Gerar um conjunto de dados de brinquedo, apenas uma linha reta com algum ruído gaussiano:
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(float)
X[X > 0] *= 4
X += 0.3 * np.random.normal(size=n_samples)

X = X[:, np.newaxis]
```
