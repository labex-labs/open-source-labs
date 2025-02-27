# Aproximación del Kernel de Chi Cuadrado Aditivo (ACS)

El kernel ACS es un kernel sobre histogramas, comúnmente utilizado en visión por computadora. La clase AdditiveChi2Sampler proporciona un mapeo aproximado para este kernel.

Para utilizar AdditiveChi2Sampler para la aproximación de kernel, siga estos pasos:

1. Inicialice el objeto AdditiveChi2Sampler con el número deseado de muestras (n) y el parámetro de regularización (c).

```python
from sklearn.kernel_approximation import AdditiveChi2Sampler

n_samples = 1000
c = 1.0
additive_chi2_sampler = AdditiveChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=2, c=c)
```

2. Ajuste el objeto AdditiveChi2Sampler a sus datos de entrenamiento.

```python
additive_chi2_sampler.fit(X_train)
```

3. Transforme sus datos de entrenamiento y prueba utilizando el objeto AdditiveChi2Sampler.

```python
X_train_transformed = additive_chi2_sampler.transform(X_train)
X_test_transformed = additive_chi2_sampler.transform(X_test)
```
