# Générer des données d'échantillonnage

Nous générons des données d'échantillonnage en créant une onde sinusoïdale avec du bruit aléatoire.

```python
n_samples = 1500
np.random.seed(0)
t = 1.5 * np.pi * (1 + 3 * np.random.rand(1, n_samples))
x = t * np.cos(t)
y = t * np.sin(t)

X = np.concatenate((x, y))
X += 0.7 * np.random.randn(2, n_samples)
X = X.T
```
