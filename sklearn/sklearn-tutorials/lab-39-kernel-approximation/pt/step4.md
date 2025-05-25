# Aproximação de Kernel Chi-Quadrado Deslocado (SCS)

O kernel SCS é uma variante do kernel chi-quadrado exponenciado que permite uma simples aproximação de Monte Carlo do mapa de características. A classe SkewedChi2Sampler fornece um mapeamento aproximado para este kernel.

Para usar o SkewedChi2Sampler para aproximação de kernel, siga estas etapas:

1. Inicialize o objeto SkewedChi2Sampler com o número desejado de amostras (n) e o parâmetro de regularização (c).

```python
from sklearn.kernel_approximation import SkewedChi2Sampler

n_samples = 1000
c = 1.0
skewed_chi2_sampler = SkewedChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=1, c=c)
```

2. Ajuste o objeto SkewedChi2Sampler aos seus dados de treinamento.

```python
skewed_chi2_sampler.fit(X_train)
```

3. Transforme seus dados de treinamento e teste usando o objeto SkewedChi2Sampler.

```python
X_train_transformed = skewed_chi2_sampler.transform(X_train)
X_test_transformed = skewed_chi2_sampler.transform(X_test)
```
