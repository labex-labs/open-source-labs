# Approximation du noyau Skewed Chi Squared (SCS)

Le noyau SCS est une variante du noyau exponentiated chi squared qui permet une approximation simple de Monte Carlo de la carte de caractéristiques. La classe SkewedChi2Sampler fournit une mappage approximatif pour ce noyau.

Pour utiliser SkewedChi2Sampler pour l'approximation de noyau, suivez ces étapes :

1. Initialisez l'objet SkewedChi2Sampler avec le nombre souhaité d'échantillons (n) et le paramètre de régularisation (c).

```python
from sklearn.kernel_approximation import SkewedChi2Sampler

n_samples = 1000
c = 1.0
skewed_chi2_sampler = SkewedChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=1, c=c)
```

2. Ajustez l'objet SkewedChi2Sampler aux données d'entraînement.

```python
skewed_chi2_sampler.fit(X_train)
```

3. Transformez vos données d'entraînement et de test à l'aide de l'objet SkewedChi2Sampler.

```python
X_train_transformed = skewed_chi2_sampler.transform(X_train)
X_test_transformed = skewed_chi2_sampler.transform(X_test)
```
