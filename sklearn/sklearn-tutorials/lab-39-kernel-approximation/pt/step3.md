# Aproximação de Kernel Aditivo Chi-Quadrado (ACS)

O kernel ACS é um kernel aplicado a histogramas, comumente utilizado em visão computacional. A classe AdditiveChi2Sampler fornece um mapeamento aproximado para este kernel.

Para usar o AdditiveChi2Sampler para aproximação de kernel, siga estas etapas:

1. Inicialize o objeto AdditiveChi2Sampler com o número desejado de amostras (n) e o parâmetro de regularização (c).

```python
from sklearn.kernel_approximation import AdditiveChi2Sampler

n_samples = 1000
c = 1.0
additive_chi2_sampler = AdditiveChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=2, c=c)
```

2. Ajuste o objeto AdditiveChi2Sampler aos seus dados de treinamento.

```python
additive_chi2_sampler.fit(X_train)
```

3. Transforme seus dados de treinamento e teste usando o objeto AdditiveChi2Sampler.

```python
X_train_transformed = additive_chi2_sampler.transform(X_train)
X_test_transformed = additive_chi2_sampler.transform(X_test)
```
