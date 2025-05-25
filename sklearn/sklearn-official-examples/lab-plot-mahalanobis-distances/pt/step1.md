# Gerar Dados

Primeiro, geramos um conjunto de dados com 125 amostras e 2 características. Ambas as características são distribuídas gaussianamente com uma média de 0. No entanto, a característica 1 tem um desvio padrão igual a 2 e a característica 2 tem um desvio padrão igual a 1. Em seguida, substituímos 25 amostras por amostras de valores discrepantes gaussianos onde a característica 1 tem um desvio padrão igual a 1 e a característica 2 tem um desvio padrão igual a 7.

```python
import numpy as np

# para resultados consistentes
np.random.seed(7)

n_samples = 125
n_outliers = 25
n_features = 2

# gerar dados gaussianos de forma (125, 2)
gen_cov = np.eye(n_features)
gen_cov[0, 0] = 2.0
X = np.dot(np.random.randn(n_samples, n_features), gen_cov)
# adicionar alguns valores discrepantes
outliers_cov = np.eye(n_features)
outliers_cov[np.arange(1, n_features), np.arange(1, n_features)] = 7.0
X[-n_outliers:] = np.dot(np.random.randn(n_outliers, n_features), outliers_cov)
```
