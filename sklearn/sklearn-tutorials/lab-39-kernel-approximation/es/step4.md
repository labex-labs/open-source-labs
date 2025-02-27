# Aproximación del Kernel de Chi Cuadrado Sesgado (SCS)

El kernel SCS es una variante del kernel de chi cuadrado exponenciado que permite una aproximación simple de Monte Carlo del mapa de características. La clase SkewedChi2Sampler proporciona un mapeo aproximado para este kernel.

Para utilizar SkewedChi2Sampler para la aproximación de kernel, siga estos pasos:

1. Inicialice el objeto SkewedChi2Sampler con el número deseado de muestras (n) y el parámetro de regularización (c).

```python
from sklearn.kernel_approximation import SkewedChi2Sampler

n_samples = 1000
c = 1.0
skewed_chi2_sampler = SkewedChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=1, c=c)
```

2. Ajuste el objeto SkewedChi2Sampler a sus datos de entrenamiento.

```python
skewed_chi2_sampler.fit(X_train)
```

3. Transforme sus datos de entrenamiento y prueba utilizando el objeto SkewedChi2Sampler.

```python
X_train_transformed = skewed_chi2_sampler.transform(X_train)
X_test_transformed = skewed_chi2_sampler.transform(X_test)
```
