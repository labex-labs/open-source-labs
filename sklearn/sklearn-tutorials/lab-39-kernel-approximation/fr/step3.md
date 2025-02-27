# Approximation du noyau Additive Chi Squared (ACS)

Le noyau ACS est un noyau sur des histogrammes, couramment utilisé en vision par ordinateur. La classe AdditiveChi2Sampler fournit une mappage approximatif pour ce noyau.

Pour utiliser AdditiveChi2Sampler pour l'approximation de noyau, suivez ces étapes :

1. Initialisez l'objet AdditiveChi2Sampler avec le nombre souhaité d'échantillons (n) et le paramètre de régularisation (c).

```python
from sklearn.kernel_approximation import AdditiveChi2Sampler

n_samples = 1000
c = 1.0
additive_chi2_sampler = AdditiveChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=2, c=c)
```

2. Ajustez l'objet AdditiveChi2Sampler aux données d'entraînement.

```python
additive_chi2_sampler.fit(X_train)
```

3. Transformez vos données d'entraînement et de test à l'aide de l'objet AdditiveChi2Sampler.

```python
X_train_transformed = additive_chi2_sampler.transform(X_train)
X_test_transformed = additive_chi2_sampler.transform(X_test)
```
